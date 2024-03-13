# myapp/myapp/doctype/tag_reader/tag_reader.py

import frappe
from frappe.model.document import Document


class TagReader(Document):

    @frappe.whitelist()
    def get_rfid_info(self):
        self.username=frappe.db.get_value("User", frappe.session.user, "full_name")
        doc = frappe.get_all("RFID Master Setting",
                            fields=["rfid_machine", "idx", "date"],
                            filters={'rfid_operator_id': frappe.session.user},
                            order_by="date desc",
                            limit=1)
       
        for d in doc:
                # if d.rfid_operator_id==frappe.session.user:
                self.reader_name=d.rfid_machine
                break
        rfidstatus=frappe.get_doc("Rfid tag Reading","rfid-tag-reading")
        # Get the Rfid tag Reading document
        # Map RFID reader names to their corresponding status attributes
        reader_status_map = {
            "RFID 1": rfidstatus.rfid1_status,
            "RFID 2": rfidstatus.rfid2_status,
            "RFID 3": rfidstatus.rfid3_status
        }

        # Get the status based on the reader name
        temp = reader_status_map.get(self.reader_name)
    
        # Display the status message with the appropriate indicator
        if temp == "Connected.":
            frappe.msgprint((self.reader_name + ' : ' + temp), indicator="green", title="RFID Status")
        else:
            frappe.msgprint((self.reader_name + ' : ' + temp), indicator="red", title="RFID Status")

        # temp1=rfidstatus.rfid1_status
        # temp2=rfidstatus.rfid2_status
        # temp3=rfidstatus.rfid3_status
        # if temp1=="Connected.":
        #     temp=temp1
        #     if self.reader_name=="RFID 1":
        #         temp=rfidstatus.rfid1_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        #     if self.reader_name=="RFID 2":
        #         temp=rfidstatus.rfid2_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        #     if self.reader_name=="RFID 3":
        #         temp=rfidstatus.rfid3_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        # else:
        #     if self.reader_name=="RFID 1":
        #         temp=rfidstatus.rfid1_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")
        #     if self.reader_name=="RFID 2":
        #         temp=rfidstatus.rfid2_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")
        #     if self.reader_name=="RFID 3":
        #         temp=rfidstatus.rfid3_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")  
                 
        # if temp2=="Connected.":
        #     temp=temp2
        #     if self.reader_name=="RFID 1":
        #         temp=rfidstatus.rfid1_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        #     if self.reader_name=="RFID 2":
        #         temp=rfidstatus.rfid2_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        #     if self.reader_name=="RFID 3":
        #         temp=rfidstatus.rfid3_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        # else:
        #     if self.reader_name=="RFID 1":
        #         temp=rfidstatus.rfid1_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")
        #     if self.reader_name=="RFID 2":
        #         temp=rfidstatus.rfid2_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")
        #     if self.reader_name=="RFID 3":
        #         temp=rfidstatus.rfid3_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")   
                
        # if temp3=="Connected.":
        #     temp=temp3
        #     if self.reader_name=="RFID 1":
        #         temp=rfidstatus.rfid1_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        #     if self.reader_name=="RFID 2":
        #         temp=rfidstatus.rfid2_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        #     if self.reader_name=="RFID 3":
        #         temp=rfidstatus.rfid3_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="green",title="RFID Status")
        # else:
        #     if self.reader_name=="RFID 1":
        #         temp=rfidstatus.rfid1_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")
        #     if self.reader_name=="RFID 2":
        #         temp=rfidstatus.rfid2_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")
        #     if self.reader_name=="RFID 3":
        #         temp=rfidstatus.rfid3_status
        #         frappe.msgprint((self.reader_name+' : '+temp),indicator="red",title="RFID Status")        
                           
    @frappe.whitelist()
    def get_rfid(self):
        doc=frappe.get_doc("Rfid tag Reading")
        if self.reader_name=="RFID 1":
            self.token_number=doc.rfid_1
        if self.reader_name=="RFID 2":
            self.token_number=doc.rfid_2
        if self.reader_name=="RFID 3":
            self.token_number=doc.rfid_3
   
                 
    @frappe.whitelist()
    def assign_tag_value(self):
        transporter = self.get('transportar')
        h_and_t_transporter = frappe.db.get_value("H and T Contract", transporter, ['name'])
        if transporter == h_and_t_transporter:
            frappe.db.set_value("H and T Contract", h_and_t_transporter, 'rfid_tag', self.token_number)
            frappe.msgprint('Setting value to H and T Contract')
        # doc=frappe.get_all("Farmer List",fields=["rfid_tag"],filters={'': frappe.session.user},limit=2)
        # frappe.db.set_value("Farmer List", self.transportar, 'rfid_tag', self.token_number)