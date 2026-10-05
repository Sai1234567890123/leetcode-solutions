/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Schedule fn to be executed after `t` milliseconds with the given args
    const timerId = setTimeout(() => {
        fn(...args);
    }, t);

    // Return a cancellation function that clears the scheduled timeout
    return function cancelFn() {
        clearTimeout(timerId);
    };
};
