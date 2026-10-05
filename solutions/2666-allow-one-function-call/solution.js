/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let hasBeenCalled = false;

    return function(...args) {
        if (!hasBeenCalled) {
            hasBeenCalled = true;
            // Use apply to preserve the execution context (`this`)
            return fn.apply(this, args);
        }
        return undefined;
    };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
