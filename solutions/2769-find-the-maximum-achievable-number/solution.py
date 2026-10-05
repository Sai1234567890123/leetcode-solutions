class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # The problem asks for the maximum possible initial value 'x' such that 'x' can become equal to
        # the given 'num' after applying a specific operation at most 't' times.

        # Let the initial value we are looking for be `x_initial`.
        # Let the given number be `num_initial`.
        # After some operations, `x_initial` becomes `x_final` and `num_initial` becomes `num_final`.
        # We want `x_final = num_final`.

        # Let's analyze the effect of the operation on the difference `x - num`.
        # The operation is: "Increase or decrease `x` by `1`, and *simultaneously* increase or decrease `num` by `1`."
        # There are four possible ways to apply this operation:

        # 1. `x` increases by 1, `num` increases by 1:
        #    - `x` becomes `x + 1`
        #    - `num` becomes `num + 1`
        #    - Effect on `x - num`: `(x + 1) - (num + 1) = x - num`. The difference remains unchanged.

        # 2. `x` decreases by 1, `num` decreases by 1:
        #    - `x` becomes `x - 1`
        #    - `num` becomes `num - 1`
        #    - Effect on `x - num`: `(x - 1) - (num - 1) = x - num`. The difference remains unchanged.

        # 3. `x` increases by 1, `num` decreases by 1:
        #    - `x` becomes `x + 1`
        #    - `num` becomes `num - 1`
        #    - Effect on `x - num`: `(x + 1) - (num - 1) = x - num + 2`. The difference increases by 2.

        # 4. `x` decreases by 1, `num` increases by 1:
        #    - `x` becomes `x - 1`
        #    - `num` becomes `num + 1`
        #    - Effect on `x - num`: `(x - 1) - (num + 1) = x - num - 2`. The difference decreases by 2.

        # Our goal is to make `x_final = num_final`, which means `x_final - num_final = 0`.
        # Let the initial difference be `D = x_initial - num_initial`.
        # We want to change this difference `D` to `0` using at most `t` operations.

        # To find the *maximum* possible `x_initial`, we want `x_initial` to be as large as possible
        # relative to `num_initial`. This implies `x_initial - num_initial` (i.e., `D`) should be
        # a positive value that we then reduce to zero.

        # If `D > 0`, we need to decrease the difference by `D`.
        # The most efficient way to decrease the difference is using operation type 4, which reduces `x - num` by 2.
        # Each such operation counts as one of the `t` allowed operations.
        # To reduce the difference `D` to `0`, we need `D / 2` operations of type 4.
        # (Note: `D` must be an even number for this to be possible, as each operation changes the difference by an even amount.
        # If `x_initial - num_initial` is odd, it can never become 0. However, our final answer will always result in an even difference.)

        # The number of operations used must be at most `t`.
        # So, `D / 2 <= t`.
        # This implies `D <= 2 * t`.

        # To maximize `x_initial`, we should choose the maximum possible value for `D`.
        # The maximum `D` is `2 * t`.
        # Substituting `D = x_initial - num_initial`:
        # `x_initial - num_initial = 2 * t`
        # `x_initial = num_initial + 2 * t`

        # Let's verify this with an example: `num = 4, t = 1`.
        # According to the formula, `x_initial = 4 + 2 * 1 = 6`.
        # Initial state: `x = 6`, `num = 4`. Difference `x - num = 2`.
        # We need to reduce the difference by 2. This requires `2/2 = 1` operation of type 4.
        # Apply operation type 4 once:
        # `x` becomes `6 - 1 = 5`
        # `num` becomes `4 + 1 = 5`
        # Now `x = 5` and `num = 5`. They are equal.
        # We used 1 operation, which is `<= t` (1 <= 1). This works.

        # The maximum achievable `x` is `num + 2 * t`.
        return num + 2 * t
