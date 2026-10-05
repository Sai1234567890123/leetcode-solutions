/**
 * Custom implementation of Array.prototype.filter.
 * 
 * @param {number[]} arr - The input array of numbers.
 * @param {Function} fn - The filtering callback function taking (element, index).
 * @return {number[]} - Array containing only elements where fn returned a truthy value.
 */
var filter = function(arr, fn) {
    const filteredArr = [];
    
    // Iterate through the array maintaining the original index
    for (let i = 0; i < arr.length; i++) {
        // Truthy check: In JavaScript, `if (condition)` implicitly evaluates Boolean(condition)
        if (fn(arr[i], i)) {
            filteredArr.push(arr[i]);
        }
    }
    
    return filteredArr;
};
