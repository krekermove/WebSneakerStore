var input_size = document.getElementsByName("size")
function sizeBtn(clickedBtn){
	if(clickedBtn.className !== "sneaker_sizes_item disabled"){
		var size_item = document.getElementsByClassName("sneaker_sizes_item")
		var tmp;
		if (getComputedStyle(clickedBtn).backgroundColor === "rgb(255, 255, 255)"){
			for (i=0;i<size_item.length;i++){
				size_item[i].className = size_item[i].className.replace(" active1", "");
			}
			clickedBtn.className += " active1";
			tmp = clickedBtn.querySelector('.size_btn');
			input_size[0].setAttribute("value", tmp.textContent);
			input_size.value = tmp.textContent;
		}
		else{
			for (i=0;i<size_item.length;i++){
				size_item[i].className = size_item[i].className.replace(" active1", "");
			}
		}
	}
}
function saveSize(){
	console.log(input_size.value);
}