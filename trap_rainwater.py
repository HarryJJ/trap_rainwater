class TrapRainwaterSolver:
    def __init__(self, heights):
        self.heights = heights

    def trap_rainwater(self):
        raise NotImplementedError("trap_rainwater method must be implemented in child classes.")


class DynamicProgrammingSolver(TrapRainwaterSolver):
    def trap_rainwater(self):
        n = len(self.heights)
        if n <= 2:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = self.heights[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], self.heights[i])

        right_max[n - 1] = self.heights[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], self.heights[i])

        water_trapped = 0
        for i in range(n):
            water_trapped += min(left_max[i], right_max[i]) - self.heights[i]

        return water_trapped


class BruteForceSolver(TrapRainwaterSolver):
    def trap_rainwater(self):
        n = len(self.heights)
        water_trapped = 0
        for i in range(1, n - 1):
            left_max = max(self.heights[:i])
            right_max = max(self.heights[i + 1:])
            water_trapped += max(0, min(left_max, right_max) - self.heights[i])
        return water_trapped


class TrapRainwaterStack(TrapRainwaterSolver):
    def trap_rainwater(self):
        stack = []
        water_trapped = 0
        for i in range(len(self.heights)):
            while stack and self.heights[i] > self.heights[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(self.heights[i], self.heights[stack[-1]]) - self.heights[top]
                water_trapped += distance * bounded_height
            stack.append(i)
        return water_trapped


class TwoPointerSolver(TrapRainwaterSolver):
    def trap_rainwater(self):
        n = len(self.heights)
        if n <= 2:
            return 0

        left = 0
        right = n - 1
        left_max = 0
        right_max = 0
        water_trapped = 0

        while left < right:
            if self.heights[left] < self.heights[right]:
                if self.heights[left] >= left_max:
                    left_max = self.heights[left]
                else:
                    water_trapped += left_max - self.heights[left]
                left += 1
            else:
                if self.heights[right] >= right_max:
                    right_max = self.heights[right]
                else:
                    water_trapped += right_max - self.heights[right]
                right -= 1

        return water_trapped
