function openModal(_header, _body) {
	
	$(".modal-head h3").html(_header);
	$(".modal-body").html(_body);
}


function addClasses(form) {
	inputData = {
		code: form.code['value'],
		cTid: form.cTid['value'],
    cSid: form.cSid['value'],
    sched: form.sched['value'],
    start: form.start['value'],
    end: form.end['value']
	}

	$.post('/addClasses', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Class "${inputData.code}" Added Successfully`, "success");
		} else {
			$.notify(`Adding class "${inputData.code}" Failed`, "error");
		}
	});
}

function editClasses(form) {
	inputData = {
		code: form.code['value'],
		cTid: form.cTid['value'],
    cSid: form.cSid['value'],
    sched: form.sched['value'],
    start: form.start['value'],
    end: form.end['value']
	}
	
	$.post('/editClasses', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Class "${inputData.code}" Edited Successfully`, "success");
		} else {
			$.notify(`Editing class "${inputData.code}" Failed`, "error");
		}
	});
}

