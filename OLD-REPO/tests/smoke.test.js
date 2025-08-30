/**
 * Smoke Tests for AI-900 Demo Application
 * Basic sanity checks to ensure the app is functional
 * Author: Tim Warner <tim@techtrainertim.com>
 */

describe('AI-900 Demo App Smoke Tests', () => {
    test('Node.js environment is working', () => {
        expect(process.version).toMatch(/^v\d+\.\d+\.\d+$/);
        expect(parseInt(process.version.slice(1))).toBeGreaterThanOrEqual(18);
    });
    
    test('Required environment variables are documented', () => {
        const requiredEnvVars = [
            'AI_SERVICES_KEY',
            'AI_SERVICES_ENDPOINT',
            'DOCUMENT_INTELLIGENCE_KEY',
            'DOCUMENT_INTELLIGENCE_ENDPOINT',
            'AZURE_OPENAI_KEY',
            'AZURE_OPENAI_ENDPOINT'
        ];
        
        // Check that sample.env exists and documents these
        const fs = require('fs');
        const sampleEnvPath = require('path').join(__dirname, '..', 'sample.env');
        const sampleEnvContent = fs.readFileSync(sampleEnvPath, 'utf-8');
        
        requiredEnvVars.forEach(envVar => {
            expect(sampleEnvContent).toContain(envVar);
        });
    });
    
    test('Console app exports required class', () => {
        const EnterpriseAI900DemoApplication = require('../app');
        expect(EnterpriseAI900DemoApplication).toBeDefined();
        expect(typeof EnterpriseAI900DemoApplication).toBe('function');
    });
    
    test('Web server exports Express app', () => {
        const app = require('../web-server');
        expect(app).toBeDefined();
        expect(typeof app.listen).toBe('function');
    });
    
    test('Package.json has all required scripts', () => {
        const packageJson = require('../package.json');
        const requiredScripts = [
            'start',
            'dev',
            'web',
            'dev:web',
            'test',
            'force-close'
        ];
        
        requiredScripts.forEach(script => {
            expect(packageJson.scripts).toHaveProperty(script);
        });
    });
    
    test('Demo assets directory exists', () => {
        const fs = require('fs');
        const path = require('path');
        const assetsPath = path.join(__dirname, '..', 'assets');
        
        expect(fs.existsSync(assetsPath)).toBe(true);
        
        // Check for key subdirectories
        const expectedDirs = ['Audio-Video', 'CSV', 'OCR', 'People', 'Places', 'Things'];
        expectedDirs.forEach(dir => {
            const dirPath = path.join(assetsPath, dir);
            expect(fs.existsSync(dirPath)).toBe(true);
        });
    });
    
    test('Critical dependencies are installed', () => {
        const packageJson = require('../package.json');
        const criticalDeps = [
            '@azure/cognitiveservices-computervision',
            '@azure/ai-text-analytics',
            '@azure/ai-form-recognizer',
            'openai',
            'express',
            'inquirer',
            'chalk',
            'dotenv'
        ];
        
        criticalDeps.forEach(dep => {
            expect(packageJson.dependencies).toHaveProperty(dep);
        });
    });
});