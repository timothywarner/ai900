/**
 * Jest Test Setup
 * AI-900 Demo Application Test Configuration
 * Author: Tim Warner <tim@techtrainertim.com>
 */

// Suppress console output during tests
const originalConsole = {
    log: console.log,
    error: console.error,
    warn: console.warn,
    info: console.info
};

// Mock environment variables for testing
process.env.NODE_ENV = 'test';
process.env.AI_SERVICES_KEY = 'test-key-12345';
process.env.AI_SERVICES_ENDPOINT = 'https://test.cognitiveservices.azure.com';
process.env.DOCUMENT_INTELLIGENCE_KEY = 'test-doc-key-12345';
process.env.DOCUMENT_INTELLIGENCE_ENDPOINT = 'https://test-doc.cognitiveservices.azure.com';
process.env.AZURE_OPENAI_KEY = 'test-openai-key-12345';
process.env.AZURE_OPENAI_ENDPOINT = 'https://test-openai.openai.azure.com';

// Global test utilities
global.testUtils = {
    // Restore console for debugging
    enableConsole: () => {
        console.log = originalConsole.log;
        console.error = originalConsole.error;
        console.warn = originalConsole.warn;
        console.info = originalConsole.info;
    },
    
    // Disable console for clean test output
    disableConsole: () => {
        console.log = jest.fn();
        console.error = jest.fn();
        console.warn = jest.fn();
        console.info = jest.fn();
    },
    
    // Simulate Azure API response delay
    simulateApiDelay: (ms = 100) => new Promise(resolve => setTimeout(resolve, ms)),
    
    // Generate mock Azure response
    generateMockAzureResponse: (success = true, data = {}) => ({
        status: success ? 200 : 400,
        statusText: success ? 'OK' : 'Bad Request',
        data: success ? data : { error: { message: 'Test error' } }
    })
};

// Disable console by default (can be enabled in specific tests)
global.testUtils.disableConsole();

// Clean up after all tests
afterAll(() => {
    global.testUtils.enableConsole();
});