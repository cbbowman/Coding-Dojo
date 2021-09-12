// Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.

function pushToFront(array, new_value) {
	for (var i = array.length; i > 0; i--) {
		array[i]=array[i-1]
	}
	array[0]=new_value
	return array
}

var array = [1,2,3,4,5]

var new_value = 7

console.log(pushToFront(array, new_value))

// Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().

function RemoveAndReturn (array) {
	var value = array[0]
	for (var i = 0, len = array.length; i < len; i++) {
		array[i] = array[i+1]
	}
	array.pop()
	return value
}

var array = [1,2,3,4,5]

console.log(RemoveAndReturn(array),array)

// Given an array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val).

function insertAtIndex(array, j, new_value) {
	for (var i = array.length; i > 0; i--) {
		if (i==j) {
			array[i] = new_value
			break
		}
		else {
			array[i]=array[i-1]
		}
		if (i==1) {
			array[0] = new_value
		}
	}
	return array
}

var array = [1,2,3,4,5]

var new_value = 7

console.log(insertAtIndex(array, 4, new_value))