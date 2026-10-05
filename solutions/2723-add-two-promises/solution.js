/**
 * @param {Promise<number>} promise1
 * @param {Promise<number>} promise2
 * @return {Promise<number>}
 */
var addTwoPromises = async function(promise1, promise2) {
    // Use 'await' to pause the execution of this async function until promise1 resolves.
    // The resolved value of promise1 (a number) will be assigned to num1.
    // Note: promise1 and promise2 start executing concurrently as soon as they are created/passed.
    // 'await' merely waits for their results without blocking other asynchronous operations.
    const num1 = await promise1;

    // Similarly, await the resolution of promise2.
    // The resolved value of promise2 (a number) will be assigned to num2.
    const num2 = await promise2;

    // Once both numbers are available, calculate their sum.
    // An async function implicitly returns a Promise that resolves with the value returned by the function.
    // So, this function will return a Promise that resolves with num1 + num2.
    return num1 + num2;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
