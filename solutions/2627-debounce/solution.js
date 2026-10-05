/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    // timerId will store the ID returned by setTimeout.
    // It needs to be declared outside the returned function to persist across calls
    // and be accessible for clearTimeout due to closure.
    let timerId;

    // Return the debounced function. This is the function that users will call.
    return function(...args) {
        // Capture the 'this' context of the current call.
        // This ensures that when 'fn' is eventually executed, it has the correct 'this' binding.
        const context = this;

        // Clear any existing timer.
        // If the debounced function is called again before 't' milliseconds have passed,
        // the previously scheduled execution of 'fn' is cancelled.
        clearTimeout(timerId);

        // Schedule a new execution of 'fn' after 't' milliseconds.
        // The 'fn' will be called with the captured 'this' context and arguments.
        timerId = setTimeout(() => {
            // Use apply to pass the captured 'this' context and arguments array to 'fn'.
            fn.apply(context, args);
        }, t);
    };
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
