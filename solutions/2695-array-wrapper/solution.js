/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
    // Precompute the sum to make valueOf() an O(1) operation
    this.sum = nums.reduce((acc, curr) => acc + curr, 0);
};

/**
 * Invoked during numeric coercion or default primitive conversion (e.g. `obj1 + obj2`).
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.sum;
};

/**
 * Invoked during string coercion (e.g. `String(obj)`).
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return `[${this.nums.join(',')}]`;
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
