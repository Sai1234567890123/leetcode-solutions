/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Invoke the function immediately with provided arguments at t = 0ms
    fn(...args);

    // Schedule subsequent invocations every t milliseconds
    const timerId = setInterval(() => {
        fn(...args);
    }, t);

    // Return the cancellation function to clear the scheduled interval
    return function cancelFn() {
        clearInterval(timerId);
    };
};
