class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class SLL {
	constructor() {
		this.head = null
	}

	addFront(value) {
		var newNode = new Node(value)
		newNode.next = this.head
		this.head = newNode
		return this
	}

	removeFront() {
		var currentNode = this.head;
		this.head = currentNode.next
		return this
	}

	front() {
		var currentNode = this.head
		if (this.head == null) {
			return null
		}
		return currentNode.value
	}

	view() {
		var currentNode = this.head;
		while (currentNode) {
			console.log(`current nodes value is ${currentNode.value}`)
			currentNode = currentNode.next
		}
	}
}

new_list = new SLL()

new_list.addFront(100)
new_list.addFront(300)
new_list.addFront(800)
new_list.view()
console.log(new_list.front())

new_list.removeFront()
new_list.view()
console.log(new_list.front())

new_list.removeFront()
new_list.view()
console.log(new_list.front())