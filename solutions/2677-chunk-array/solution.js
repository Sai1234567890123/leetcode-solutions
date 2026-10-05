/**
 * Chunks an array into subarrays of specified size.
 * 
 * @param {Array} arr - The array to process.
 * @param {number} size - The length of each chunk.
 * @return {Array} - The array of chunks.
 */
var chunk = function(arr, size) {
    const chunked = [];
    
    // Step through the array in strides of `size`
    for (let i = 0; i < arr.length; i += size) {
        // Array.prototype.slice handles out-of-bound indices gracefully
        // by slicing up to arr.length without throwing an error
        chunked.push(arr.slice(i, i + size));
    }
    
    return chunked;
};
