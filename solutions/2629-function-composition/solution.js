/**
 * Composes an array of functions from right to left.
 *
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        // Iterate from right to left to evaluate functions in composition order:
        // fn(x) = f1(f2(...fn(x)))
        let result = x;
        for (let i = functions.length - 1; i >= 0; i--) {
            result = functions[i](result);
        }
        return result;
    };
};
