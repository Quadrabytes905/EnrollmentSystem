function openModal(_header, _body) {
	
	$(".modal-head h3").html(_header);
	$(".modal-body").html(_body);
}


function addSubjects(form) {
	inputData = {
		subjID: form.subjID['value'],
		subjName: form.subjName['value']
	}

	$.post('/addSubjects', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Subjects "${inputData.subjID}" Added Successfully`, "success");
		} else {
			$.notify(`Adding subjects "${inputData.subjID}" Failed`, "error");
		}
	});
}

function editSubjects(form) {
	inputData = {
		subjID: form.subjID['value'],
		subjName: form.subjName['value']
	}
	
	$.post('/editSubjects', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Subjects "${inputData.subjID}" Edited Successfully`, "success");
		} else {
			$.notify(`Editing subject "${inputData.subjID}" Failed`, "error");
		}
	});
}

