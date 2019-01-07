function enroll(value) {
    inputData = {
        stubCode: value
    }

    $.post("/enrollSubject", inputData,
        function (data) {
            if (data == 'True') {
                $.notify(`Successfully Enroll StubCode = ${value}`, "success");
            } else {
                $.notify("Can't enroll", "error");
            }
    });
}

function rateTeacher(form) {
	inputData = {
		teacherID: form.teacherSelect['value'],
		rating: form.rateNum['value'],
		comment: form.comment['value']
    }

    console.log(inputData);
    
	$.post('/saveRating', inputData, function(data) {
		if (data == 'success') {
			$.notify(`Teacher "${inputData.teacherID}" Rated Successfully`, "success");
		} else {
			$.notify('Rating Failed', "error");
		}
	});
}

function getClassTeacherRating(_subjectID) {
    inputData = {
        subjectID: _subjectID
    }

    $.post("/subjectTeachers", inputData,
        function (data) {
            $(".special").html(data);
    });
}

