/**
 * Sorts an array in ascending order based on the output of a mapping function.
 *
 * @param {Array} arr - The array of items to sort.
 * @param {Function} fn - Function that returns a numeric key for each item.
 * @return {Array} - The sorted array.
 */
var sortBy = function(arr, fn) {
    // Array.prototype.sort takes a comparator function (a, b).
    // Comparing fn(a) - fn(b) sorts elements in ascending order of their fn values.
    // If fn(a) < fn(b), result is negative -> 'a' comes before 'b'.
    // If fn(a) > fn(b), result is positive -> 'b' comes before 'a'.
    return arr.sort((a, b) => fn(a) - fn(b));
};
