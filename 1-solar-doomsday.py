def solution(area):
  result = []
  while area > 0:
    value = int(area ** 0.5)
    square = value ** 2
    result.append(square)
    area -= square
  return result