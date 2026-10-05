/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    // The rest parameter '...args' collects all arguments passed to the function
    // into a single array named 'args'.
    // To find the count of arguments, we simply need to return the length of this array.
    return args.length;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
