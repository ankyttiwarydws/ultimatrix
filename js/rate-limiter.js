// Simple client-side rate limiter
class RateLimiter {
    constructor() {
        this.attempts = new Map();
        this.maxAttempts = 5;
        this.timeWindow = 60000; // 1 minute
    }

    isAllowed(action, identifier = 'default') {
        const key = `${action}_${identifier}`;
        const now = Date.now();

        if (!this.attempts.has(key)) {
            this.attempts.set(key, []);
        }

        const attempts = this.attempts.get(key);

        // Remove old attempts outside time window
        const validAttempts = attempts.filter(time => now - time < this.timeWindow);
        this.attempts.set(key, validAttempts);

        if (validAttempts.length >= this.maxAttempts) {
            return false;
        }

        // Add current attempt
        validAttempts.push(now);
        return true;
    }

    getRemainingTime(action, identifier = 'default') {
        const key = `${action}_${identifier}`;
        const attempts = this.attempts.get(key) || [];
        if (attempts.length === 0) return 0;

        const oldestAttempt = Math.min(...attempts);
        const remaining = this.timeWindow - (Date.now() - oldestAttempt);
        return Math.max(0, remaining);
    }
}

// Global rate limiter instance
const rateLimiter = new RateLimiter();

// Example usage for form submissions
function handleFormSubmission(event, formType = 'contact') {
    if (!rateLimiter.isAllowed('form_submit', formType)) {
        event.preventDefault();
        const remainingTime = Math.ceil(rateLimiter.getRemainingTime('form_submit', formType) / 1000);
        alert(`Too many attempts. Please wait ${remainingTime} seconds before trying again.`);
        return false;
    }
    return true;
}

// Example usage for game actions
function handleGameAction(action) {
    if (!rateLimiter.isAllowed('game_action', action)) {
        console.log('Rate limit exceeded for game action:', action);
        return false;
    }
    return true;
}