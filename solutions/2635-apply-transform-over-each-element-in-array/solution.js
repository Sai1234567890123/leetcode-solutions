/**
 * Applies a transformation function over each element in an array.
 * 
 * @param {number[]} arr - The input array of integers.
 * @param {Function} fn - The mapping function taking (element, index) and returning a transformed value.
 * @return {number[]} - The newly constructed transformed array.
 */
var map = function(arr, fn) {
    const len = arr.length;
    // Pre-allocate the exact length to prevent dynamic array resizing in V8.
    const result = new Array(len);
    
    for (let i = 0; i < len; i++) {
        // Apply mapping function with current element and current index
        result[i] = fn(arr[i], i);
    }
    
    return result;
};
