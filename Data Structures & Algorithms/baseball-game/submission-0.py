class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for i in operations:
            try:
                num = int(i)
                score.append(num)
            except:
                if i == "+":
                    action = score[-1] + score[-2]
                    score.append(action)
                elif i == 'D':
                    action = score[-1] * 2
                    score.append(action)
                else:
                    score.pop()
            print(score)
        return sum(score)