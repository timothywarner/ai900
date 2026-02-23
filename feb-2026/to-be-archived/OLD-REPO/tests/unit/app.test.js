/**
 * Unit Tests for AI-900 Console Application
 * Tests cover all critical functionality for certification prep
 * Author: Tim Warner <tim@techtrainertim.com>
 */

const EnterpriseAI900DemoApplication = require('../../app');

// Mock all Azure SDK modules
jest.mock('@azure/cognitiveservices-computervision');
jest.mock('@azure/ms-rest-azure-js');
jest.mock('@azure/ai-text-analytics');
jest.mock('@azure/ai-form-recognizer');
jest.mock('openai');
jest.mock('inquirer');
jest.mock('fs').promises;

describe('EnterpriseAI900DemoApplication', () => {
    let app;
    let mockInquirer;
    
    beforeEach(() => {
        jest.clearAllMocks();
        app = new EnterpriseAI900DemoApplication();
        mockInquirer = require('inquirer');
    });
    
    describe('Core Application Setup', () => {
        test('should initialize with correct default values', () => {
            expect(app.isApplicationRunning).toBe(true);
            expect(app.serviceHealthMetrics).toBeInstanceOf(Map);
            expect(app.operationMetrics).toEqual({
                totalOperations: 0,
                successfulOperations: 0,
                failedOperations: 0,
                retryAttempts: 0,
                averageResponseTime: 0
            });
        });
        
        test('should handle missing environment variables gracefully', () => {
            const originalEnv = process.env;
            process.env = {};
            
            const appWithoutEnv = new EnterpriseAI900DemoApplication();
            expect(appWithoutEnv.serviceHealthMetrics.size).toBe(0);
            
            process.env = originalEnv;
        });
    });
    
    describe('Retry Logic Implementation', () => {
        test('should retry failed operations with exponential backoff', async () => {
            let attemptCount = 0;
            const failingOperation = jest.fn().mockImplementation(() => {
                attemptCount++;
                if (attemptCount < 3) {
                    throw new Error('Transient error');
                }
                return { success: true };
            });
            
            // Import the retry function from the module
            const { executeAzureAIOperationWithRetry } = require('../../app');
            
            const result = await executeAzureAIOperationWithRetry(
                failingOperation,
                'Test Operation',
                { MAX_RETRY_ATTEMPTS: 3, INITIAL_RETRY_DELAY_MS: 10 }
            );
            
            expect(result).toEqual({ success: true });
            expect(failingOperation).toHaveBeenCalledTimes(3);
        });
        
        test('should handle rate limiting (429) errors specially', async () => {
            const rateLimitError = new Error('Rate limited');
            rateLimitError.status = 429;
            
            const rateLimitedOperation = jest.fn()
                .mockRejectedValueOnce(rateLimitError)
                .mockResolvedValueOnce({ success: true });
            
            const { executeAzureAIOperationWithRetry } = require('../../app');
            
            const result = await executeAzureAIOperationWithRetry(
                rateLimitedOperation,
                'Rate Limited Operation',
                { RATE_LIMIT_RETRY_DELAY_MS: 10 }
            );
            
            expect(result).toEqual({ success: true });
            expect(rateLimitedOperation).toHaveBeenCalledTimes(2);
        });
        
        test('should fail after max retry attempts', async () => {
            const alwaysFailingOperation = jest.fn()
                .mockRejectedValue(new Error('Persistent error'));
            
            const { executeAzureAIOperationWithRetry } = require('../../app');
            
            await expect(
                executeAzureAIOperationWithRetry(
                    alwaysFailingOperation,
                    'Always Failing Operation',
                    { MAX_RETRY_ATTEMPTS: 2, INITIAL_RETRY_DELAY_MS: 10 }
                )
            ).rejects.toThrow('Persistent error');
            
            expect(alwaysFailingOperation).toHaveBeenCalledTimes(2);
        });
    });
    
    describe('Input Validation and Sanitization', () => {
        test('should validate and sanitize user input correctly', () => {
            const { validateAndSanitizeUserInput } = require('../../app');
            
            const validInput = 'This is a valid test input';
            const result = validateAndSanitizeUserInput(validInput);
            
            expect(result).toEqual({
                original: validInput,
                sanitized: validInput,
                isValid: true,
                length: validInput.length,
                sanitizedContent: false
            });
        });
        
        test('should detect and sanitize malicious content', () => {
            const { validateAndSanitizeUserInput } = require('../../app');
            
            const maliciousInput = '<script>alert("xss")</script>Some text';
            const result = validateAndSanitizeUserInput(maliciousInput);
            
            expect(result.sanitized).toBe('alert("xss")Some text');
            expect(result.sanitizedContent).toBe(true);
        });
        
        test('should reject input exceeding maximum length', () => {
            const { validateAndSanitizeUserInput } = require('../../app');
            
            const longInput = 'a'.repeat(6000);
            expect(() => validateAndSanitizeUserInput(longInput))
                .toThrow('Input exceeds maximum length');
        });
        
        test('should reject non-string input', () => {
            const { validateAndSanitizeUserInput } = require('../../app');
            
            expect(() => validateAndSanitizeUserInput(null))
                .toThrow('Input must be a non-empty string');
            expect(() => validateAndSanitizeUserInput(123))
                .toThrow('Input must be a non-empty string');
        });
    });
    
    describe('Computer Vision Capabilities', () => {
        test('should analyze images with proper error handling', async () => {
            const mockVisionClient = {
                analyzeImageInStream: jest.fn().mockResolvedValue({
                    description: { captions: [{ text: 'Test image', confidence: 0.95 }] },
                    tags: [{ name: 'test', confidence: 0.9 }],
                    objects: [{ object: 'item', rectangle: { x: 0, y: 0, w: 100, h: 100 } }],
                    faces: [{ gender: 'male', age: 30 }],
                    adult: { isAdultContent: false, adultScore: 0.1, isRacyContent: false, racyScore: 0.1 }
                })
            };
            
            // Mock the client
            require('@azure/cognitiveservices-computervision').ComputerVisionClient
                .mockImplementation(() => mockVisionClient);
            
            const fs = require('fs').promises;
            fs.readFile = jest.fn().mockResolvedValue(Buffer.from('fake-image-data'));
            
            // Create app and test
            const testApp = new EnterpriseAI900DemoApplication();
            testApp.cognitiveVisionClient = mockVisionClient;
            testApp.waitForUserInput = jest.fn().mockResolvedValue();
            
            await testApp.demonstrateComputerVisionCapabilities();
            
            expect(mockVisionClient.analyzeImageInStream).toHaveBeenCalled();
            expect(testApp.waitForUserInput).toHaveBeenCalled();
        });
    });
    
    describe('Language Analytics Capabilities', () => {
        test('should perform sentiment analysis on customer feedback', async () => {
            const mockLanguageClient = {
                analyzeSentiment: jest.fn().mockResolvedValue([{
                    sentiment: 'positive',
                    confidenceScores: { positive: 0.95, negative: 0.03, neutral: 0.02 }
                }]),
                detectLanguage: jest.fn().mockResolvedValue([{
                    primaryLanguage: { name: 'English', iso6391Name: 'en', confidenceScore: 0.99 }
                }]),
                extractKeyPhrases: jest.fn().mockResolvedValue([{
                    keyPhrases: ['customer service', 'quality', 'products']
                }])
            };
            
            require('@azure/ai-text-analytics').TextAnalyticsClient
                .mockImplementation(() => mockLanguageClient);
            
            const testApp = new EnterpriseAI900DemoApplication();
            testApp.languageAnalyticsClient = mockLanguageClient;
            testApp.waitForUserInput = jest.fn().mockResolvedValue();
            
            await testApp.demonstrateLanguageAnalyticsCapabilities();
            
            expect(mockLanguageClient.analyzeSentiment).toHaveBeenCalled();
            expect(mockLanguageClient.detectLanguage).toHaveBeenCalled();
            expect(mockLanguageClient.extractKeyPhrases).toHaveBeenCalled();
        });
    });
    
    describe('Azure OpenAI Integration', () => {
        test('should generate chat completions with responsible AI', async () => {
            const mockOpenAIClient = {
                chat: {
                    completions: {
                        create: jest.fn().mockResolvedValue({
                            choices: [{
                                message: { content: 'Generated response from AI' }
                            }]
                        })
                    }
                }
            };
            
            require('openai').OpenAI.mockImplementation(() => mockOpenAIClient);
            
            const testApp = new EnterpriseAI900DemoApplication();
            testApp.azureOpenAIClient = mockOpenAIClient;
            testApp.waitForUserInput = jest.fn().mockResolvedValue();
            
            await testApp.demonstrateAzureOpenAICapabilities();
            
            expect(mockOpenAIClient.chat.completions.create).toHaveBeenCalled();
            const callArgs = mockOpenAIClient.chat.completions.create.mock.calls[0][0];
            expect(callArgs.messages[0].role).toBe('system');
            expect(callArgs.messages[0].content).toContain('responsible AI');
        });
    });
    
    describe('Service Health Metrics', () => {
        test('should track and display service health metrics', () => {
            const testApp = new EnterpriseAI900DemoApplication();
            
            // Set up mock metrics
            testApp.serviceHealthMetrics.set('TestService', { status: 'healthy', endpoint: 'https://test.com' });
            testApp.operationMetrics = {
                totalOperations: 100,
                successfulOperations: 95,
                failedOperations: 5,
                retryAttempts: 10,
                averageResponseTime: 250
            };
            
            // Spy on console.log to verify output
            const consoleSpy = jest.spyOn(console, 'log').mockImplementation();
            
            testApp.displayServiceHealthAndMetrics();
            
            // Verify metrics are displayed
            expect(consoleSpy).toHaveBeenCalledWith(expect.stringContaining('TestService'));
            expect(consoleSpy).toHaveBeenCalledWith(expect.stringContaining('95%')); // Success rate
            
            consoleSpy.mockRestore();
        });
    });
    
    describe('Menu Navigation', () => {
        test('should display menu and handle user selections', async () => {
            mockInquirer.prompt.mockResolvedValueOnce({ selectedChoice: 'computer_vision' })
                .mockResolvedValueOnce({ continue: '' })
                .mockResolvedValueOnce({ selectedChoice: 'exit_application' });
            
            const testApp = new EnterpriseAI900DemoApplication();
            testApp.demonstrateComputerVisionCapabilities = jest.fn().mockResolvedValue();
            
            await testApp.run();
            
            expect(testApp.demonstrateComputerVisionCapabilities).toHaveBeenCalled();
            expect(testApp.isApplicationRunning).toBe(false);
        });
    });
    
    describe('Error Handling', () => {
        test('should handle Azure service errors gracefully', async () => {
            const mockError = new Error('Azure service unavailable');
            mockError.status = 503;
            
            const failingClient = {
                analyzeImageInStream: jest.fn().mockRejectedValue(mockError)
            };
            
            const testApp = new EnterpriseAI900DemoApplication();
            testApp.cognitiveVisionClient = failingClient;
            testApp.waitForUserInput = jest.fn().mockResolvedValue();
            
            // Should not throw
            await expect(testApp.demonstrateComputerVisionCapabilities())
                .resolves.not.toThrow();
            
            expect(testApp.waitForUserInput).toHaveBeenCalled();
        });
    });
});

// Export retry function for testing
module.exports.executeAzureAIOperationWithRetry = require('../../app').executeAzureAIOperationWithRetry;
module.exports.validateAndSanitizeUserInput = require('../../app').validateAndSanitizeUserInput;