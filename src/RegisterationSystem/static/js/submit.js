function submit(){
	var input1=document.getElementById('Content_name');
	var input2=document.getElementById('Content_Grade');
	var input3=document.getElementById('Content_StuNo');
	var input4=document.getElementById('Content_CellPhone');
	if(!input4.value){
		input4.focus();
	}
	if(!input3.value){
		input3.focus();
	}
	if(!input2.value){
		input2.focus();
	}
	if(!input1.value){
		input1.focus();
	}
	if(input1.value&&input2.value&&input3.value&&input4.value)
	{
		document.getElementById('form1').submit();
	}
}