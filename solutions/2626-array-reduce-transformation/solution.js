/**
 * Executes a reducer function sequentially on each element of an array,
 * passing the accumulated result to the next iteration.
 *
 * @param {number[]} nums - Array of integers to reduce.
 * @param {Function} fn - Reducer callback: fn(accumulator, currentValue).
 * @param {number} init - Initial value for the accumulator.
 * @return {number} - Final accumulated result.
 */
var reduce = function(nums, fn, init) {
    let accumulator = init;

    // Use a classic indexed for-loop for maximum performance in V8
    for (let i = 0; i < nums.length; i++) {
        accumulator = fn(accumulator, nums[i]);
    }

    return accumulator;
};
