function openModal(_header, _body) {
	
	$(".modal-head h3").html(_header);
	$(".modal-body").html(_body);
}

function addStudent(form) {
	inputData = {
		id: form.studentID['value'],
		fname: form.firstName['value'],
		lname: form.lastName['value'],
		course: form.course['value'],
		year: form.year['value']
	}

	$.post('/addStudent', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Student "${inputData.id}" Added Successfully`, "success");
		} else {
			$.notify(`Adding student "${inputData.id}" Failed`, "error");
		}
	});
}


function editStudent(form) {
	inputData = {
		id: form.studentID['value'],
		fname: form.firstName['value'],
		lname: form.lastName['value'],
		course: form.course['value'],
		year: form.year['value']
	}
	
	$.post('/editStudent', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Student "${inputData.id}" Edited Successfully`, "success");
		} else {
			$.notify(`Editing student "${inputData.id}" Failed`, "error");
		}
	});
}
