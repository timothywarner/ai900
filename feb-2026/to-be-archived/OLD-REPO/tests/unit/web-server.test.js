/**
 * Unit Tests for AI-900 Web Server
 * Tests cover all web API endpoints and functionality
 * Author: Tim Warner <tim@techtrainertim.com>
 */

const request = require('supertest');
const app = require('../../web-server');

// Mock multer for file uploads
jest.mock('multer', () => {
    const multer = () => ({
        single: () => (req, res, next) => {
            req.file = { filename: 'test.jpg', mimetype: 'image/jpeg', size: 1000 };
            next();
        }
    });
    multer.memoryStorage = jest.fn();
    return multer;
});

describe('AI-900 Web Server', () => {
    describe('GET /', () => {
        test('should return Contoso AI Portal HTML page', async () => {
            const response = await request(app).get('/');
            
            expect(response.status).toBe(200);
            expect(response.text).toContain('Contoso AI Portal');
            expect(response.text).toContain('Azure AI-900 Demo');
            expect(response.text).toContain('Tim Warner');
        });
        
        test('should include all AI service cards', async () => {
            const response = await request(app).get('/');
            
            const services = [
                'Computer Vision',
                'Language Service',
                'Document Intelligence',
                'Speech Services',
                'Azure OpenAI',
                'Cognitive Search'
            ];
            
            services.forEach(service => {
                expect(response.text).toContain(service);
            });
        });
    });
    
    describe('POST /api/vision/analyze', () => {
        test('should analyze uploaded image successfully', async () => {
            const response = await request(app)
                .post('/api/vision/analyze')
                .attach('image', Buffer.from('fake-image-data'), 'test.jpg');
            
            expect(response.status).toBe(200);
            expect(response.body).toEqual({
                success: true,
                description: expect.stringContaining('Contoso'),
                tags: expect.any(String),
                objects: expect.any(String)
            });
        });
        
        test('should handle missing image file', async () => {
            const response = await request(app)
                .post('/api/vision/analyze')
                .send({});
            
            expect(response.status).toBe(200);
            expect(response.body).toEqual({
                success: false,
                error: 'No image file provided'
            });
        });
    });
    
    describe('POST /api/language/analyze', () => {
        test('should analyze positive sentiment correctly', async () => {
            const response = await request(app)
                .post('/api/language/analyze')
                .send({ text: 'I love the excellent Contoso products! Amazing quality!' });
            
            expect(response.status).toBe(200);
            expect(response.body).toEqual({
                success: true,
                sentiment: 'positive',
                confidence: expect.any(Number),
                language: 'English',
                keyPhrases: expect.stringContaining('Contoso')
            });
            expect(response.body.confidence).toBeGreaterThan(60);
        });
        
        test('should analyze negative sentiment correctly', async () => {
            const response = await request(app)
                .post('/api/language/analyze')
                .send({ text: 'Terrible experience with awful products. Very disappointed and frustrated.' });
            
            expect(response.status).toBe(200);
            expect(response.body).toEqual({
                success: true,
                sentiment: 'negative',
                confidence: expect.any(Number),
                language: 'English',
                keyPhrases: expect.any(String)
            });
        });
        
        test('should analyze neutral sentiment correctly', async () => {
            const response = await request(app)
                .post('/api/language/analyze')
                .send({ text: 'The product exists and functions as described.' });
            
            expect(response.status).toBe(200);
            expect(response.body.sentiment).toBe('neutral');
        });
        
        test('should handle missing text input', async () => {
            const response = await request(app)
                .post('/api/language/analyze')
                .send({});
            
            expect(response.status).toBe(200);
            expect(response.body).toEqual({
                success: false,
                error: 'No text provided'
            });
        });
    });
    
    describe('POST /api/openai/chat', () => {
        test('should generate AI response for valid prompt', async () => {
            const response = await request(app)
                .post('/api/openai/chat')
                .send({ prompt: 'Tell me about Contoso products' });
            
            expect(response.status).toBe(200);
            expect(response.body).toEqual({
                success: true,
                response: expect.stringContaining('Contoso')
            });
        });
        
        test('should handle missing prompt', async () => {
            const response = await request(app)
                .post('/api/openai/chat')
                .send({});
            
            expect(response.status).toBe(200);
            expect(response.body).toEqual({
                success: false,
                error: 'No prompt provided'
            });
        });
    });
    
    describe('GET /health', () => {
        test('should return health check status', async () => {
            const response = await request(app).get('/health');
            
            expect(response.status).toBe(200);
            expect(response.body).toEqual({
                status: 'healthy',
                service: 'Contoso AI Portal',
                timestamp: expect.stringMatching(/^\d{4}-\d{2}-\d{2}T/)
            });
        });
    });
    
    describe('Static Asset Serving', () => {
        test('should serve assets directory', async () => {
            const response = await request(app).get('/assets/test.txt');
            
            // Will get 404 since file doesn't exist, but route is configured
            expect(response.status).toBe(404);
        });
    });
    
    describe('Error Handling', () => {
        test('should handle API errors gracefully', async () => {
            // Mock an internal error
            const originalPost = app.post;
            app.post = jest.fn().mockImplementation((path, ...handlers) => {
                if (path === '/api/test-error') {
                    return originalPost.call(app, path, (req, res) => {
                        throw new Error('Test error');
                    });
                }
                return originalPost.call(app, path, ...handlers);
            });
            
            const response = await request(app)
                .post('/api/test-error')
                .send({});
            
            // Express default error handler returns 500
            expect(response.status).toBe(500);
            
            app.post = originalPost;
        });
    });
    
    describe('Content Type Handling', () => {
        test('should accept JSON content', async () => {
            const response = await request(app)
                .post('/api/language/analyze')
                .set('Content-Type', 'application/json')
                .send({ text: 'Test text' });
            
            expect(response.status).toBe(200);
            expect(response.type).toBe('application/json');
        });
        
        test('should handle large payloads within limit', async () => {
            const largeText = 'a'.repeat(5000); // Within 10mb limit
            
            const response = await request(app)
                .post('/api/language/analyze')
                .send({ text: largeText });
            
            expect(response.status).toBe(200);
        });
    });
    
    describe('CORS and Security Headers', () => {
        test('should set appropriate headers', async () => {
            const response = await request(app).get('/health');
            
            // Basic security headers that should be set
            expect(response.headers['x-powered-by']).toBeUndefined(); // Express hides this by default
        });
    });
});

// Integration test for full user flow
describe('Integration Tests', () => {
    test('should handle complete user journey', async () => {
        // 1. Load home page
        let response = await request(app).get('/');
        expect(response.status).toBe(200);
        
        // 2. Analyze text
        response = await request(app)
            .post('/api/language/analyze')
            .send({ text: 'Great Contoso service!' });
        expect(response.body.success).toBe(true);
        expect(response.body.sentiment).toBe('positive');
        
        // 3. Chat with AI
        response = await request(app)
            .post('/api/openai/chat')
            .send({ prompt: 'Hello AI' });
        expect(response.body.success).toBe(true);
        
        // 4. Check health
        response = await request(app).get('/health');
        expect(response.body.status).toBe('healthy');
    });
});