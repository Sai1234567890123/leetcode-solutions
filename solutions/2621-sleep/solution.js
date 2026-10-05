/**
 * Asynchronously pauses execution for the specified duration.
 *
 * @param {number} millis - The number of milliseconds to sleep.
 * @return {Promise<void>} A promise that resolves after millis milliseconds.
 */
async function sleep(millis) {
    // Return a Promise that resolves when setTimeout completes after `millis` ms.
    return new Promise(resolve => setTimeout(resolve, millis));
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
