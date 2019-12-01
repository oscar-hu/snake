class Snake:
	def __init__(self, pos, w, h): # pos is for the head
		self.pos = pos
		self.body = []
		self.width = w
		self.height = h

	def grow(self, direction, winX, winY): # 0 = up, 1 = down, 2 = left, 3 = right
		currX = self.pos[0] #tail X coordinate
		currY = self.pos[1] #tail Y coordinate

		if self.body:
			length = len(self.body)
			tail = self.body[length - 1]
			currX, currY = tail[0], tail[1]

		bodyX, bodyY = 0, 0
		if direction == 0:
			bodyX = currX
			bodyY = currY + self.height
		if direction == 1:
			bodyX = currX
			bodyY = currY - self.height
		if direction == 2:
			bodyX = currX + self.width
			bodyY = currY
		if direction == 3:
			bodyX = currX - self.width
			bodyY = currY
		self.body.append([bodyX % winX, bodyY % winY])

	def updatePos(self, x, y):
		tailIndex = len(self.body) - 1
		while tailIndex >= 1:
			self.body[tailIndex] = self.body[tailIndex - 1]
			tailIndex -= 1
		if self.body:
			self.body[0] = self.pos
		self.pos = [x, y]\

	def length(self):
		return len(self.body) + 1