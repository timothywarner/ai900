/**
 * Jest Configuration for AI-900 Demo Application
 * Educational testing setup for Azure AI services
 * Author: Tim Warner <tim@techtrainertim.com>
 */

module.exports = {
    // Test environment setup
    testEnvironment: 'node',
    
    // Coverage configuration
    collectCoverage: true,
    coverageDirectory: 'coverage',
    coverageThreshold: {
        global: {
            branches: 50,
            functions: 50,
            lines: 50,
            statements: 50
        }
    },
    
    // Test patterns
    testMatch: [
        '**/tests/**/*.test.js',
        '**/__tests__/**/*.js'
    ],
    
    // Files to ignore
    testPathIgnorePatterns: [
        '/node_modules/',
        '/assets/',
        '/docs/'
    ],
    
    // Setup files
    setupFilesAfterEnv: ['<rootDir>/tests/setup.js'],
    
    // Module name mapping
    moduleNameMapper: {},
    
    // Transform configuration
    transform: {},
    
    // Test timeout for Azure API calls
    testTimeout: 30000,
    
    // Verbose output for educational purposes
    verbose: true,
    
    // Clear mocks between tests
    clearMocks: true,
    
    // Restore mocks between tests
    restoreMocks: true,
    
    // Coverage reporters
    coverageReporters: ['text', 'lcov', 'html'],
    
    // Files to collect coverage from
    collectCoverageFrom: [
        'app.js',
        'web-server.js',
        '!**/node_modules/**',
        '!**/tests/**',
        '!**/coverage/**'
    ]
};