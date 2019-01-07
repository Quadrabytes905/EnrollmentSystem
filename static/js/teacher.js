function openModal(_header, _body) {
	
	$(".modal-head h3").html(_header);
	$(".modal-body").html(_body);
}


function addTeacher(form) {
	inputData = {
		tid: form.teacherID['value'],
		tfname: form.firstName['value'],
		tlname: form.lastName['value']
	}

	$.post('/addTeacher', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Teacher "${inputData.tid}" Added Successfully`, "success");
		} else {
			$.notify(`Adding teacher "${inputData.tid}" Failed`, "error");
		}
	});
}

function editTeacher(form) {
	inputData = {
		tid: form.teacherID['value'],
		tfname: form.firstName['value'],
		tlname: form.lastName['value']
	}
	
	$.post('/editTeacher', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Teacher "${inputData.tid}" Edited Successfully`, "success");
		} else {
			$.notify(`Editing teacher "${inputData.tid}" Failed`, "error");
		}
	});
}

