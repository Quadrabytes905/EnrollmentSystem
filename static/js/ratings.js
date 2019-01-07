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