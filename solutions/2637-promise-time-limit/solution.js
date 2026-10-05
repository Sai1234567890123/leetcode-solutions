/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        let timerId;
        
        // Create a promise that rejects after `t` milliseconds
        const timeoutPromise = new Promise((_, reject) => {
            timerId = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
        });

        try {
            // Race the original async function against the timeout promise
            return await Promise.race([fn(...args), timeoutPromise]);
        } finally {
            // Clean up the timer to prevent memory leaks and pending operations
            clearTimeout(timerId);
        }
    };
};
