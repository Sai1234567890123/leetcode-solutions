/**
 * Generates the Fibonacci sequence infinitely using a generator function.
 * 
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let current = 0;
    let next = 1;

    while (true) {
        // Yield the current Fibonacci number
        yield current;
        // Update values for the next iteration using destructuring assignment
        [current, next] = [next, current + next];
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
