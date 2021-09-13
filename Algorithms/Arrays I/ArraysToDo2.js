// Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second array – move values within the array that you are given. As always, do not use built-in array functions such as splice().

function reverseArray(array) {
	var len = array.length
	var half = len/2
	var temp
	for (var i=0; i<half; i++) {
		temp = array[i]
		array[i]=array[(len-i)-1]
		array[(len-i)-1]=temp
	}
	return array
}

array1 = [1,2,3,4,5,6,7]
array2 = [1,2,3,4,5,6,7,8]

console.log(reverseArray(array1))
console.log(reverseArray(array2))

// Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), change the array to [3,1,2]. Don't use built-in functions.
// Second: allow negative shiftBy (shift L, not R).
// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
// Fourth: minimize the touches of each element.

function rotateArr(arr, shiftBy) {
	if (shiftBy<0) {
		return rotateArr(arr, (arr.length)+shiftBy)
	}

	if(shiftBy==0) {
		return arr
	}

	if(shiftBy>arr.length) {
		shiftBy = shiftBy % (arr.length)
	}

	var temp = arr[arr.length - 1]
	for (var i=1; i<(arr.length); i++) {
		arr[arr.length-i] = arr[arr.length-i-1]
	}
	arr[0] = temp
	return rotateArr(arr, shiftBy-1)
}

array = [1,2,3,4,5,6]
console.log(rotateArr(array,2))

// Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.

function filterArray(arr, min, max) {
	var new_length = arr.length
	for(var i=0, j=0; i< arr.length; i++) {
		if ((arr[i]>=min)&&(arr[i]<=max)){
			arr[j]=arr[i]
			j++
		}
		else {
			new_length--
		}
	}
	arr.length = new_length
	return arr
}

console.log(filterArray([2,4,2,8,4,52,4,5,1,0],3,8))

// Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].

function arrConcat(arr1, arr2) {
	len1 = arr1.length
	arr1.length += arr2.length
	for (var i=0; i<arr2.length; i++) {
		arr1[i+len1]=arr2[i]
	}
	return arr1
}

console.log(arrConcat(['a','b'], [1,2]))