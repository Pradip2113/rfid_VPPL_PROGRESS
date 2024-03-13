// Copyright (c) 2023, soham.pawar@erpdata.in and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tag Reader', {
	onload(frm) {
            frm.call({
				method:'get_rfid_info',
				doc:frm.doc,
				
			}) 
	 },
	 start_reading:function(frm) {
		frm.call({
			method:'get_rfid',
			doc:frm.doc,
			
		}) 
 },
	 after_save(frm) {
		frm.call({
			method:'assign_tag_value',
			doc:frm.doc,
		}) 
 }

});
