# THIS PROGRAM WAS WRITTEN TO GENERATE A PDF INVOICE FOR SERVICES, ETC.



############################################### CLASSES ###############################################

# Make a class for the invoice
class invoice:
	def __init__(self, number, company, company_address, date, bill_to_company, bill_to_company_address, product_description, payment_date, payment_method):
		self.number = number
		self.company = company
		self.company_address = company_address
		self.date = date
		self.bill_to_company = bill_to_company
		self.bill_to_company_address = bill_to_company_address
		self.product_description = product_description
		self.invoice_items = []
		self.invoice_subtotal = 0
		self.invoice_taxes = 0
		self.invoice_other_fees = 0
		self.invoice_total = 0
		self.payment_date = payment_date
		self.payment_method = payment_method

	def add_item(self,invoice_item):
		self.invoice_items.append(invoice_item)
		return print(invoice_item.item_description + "successfully added to invoice.")

	def calculate_totals(self):
		invoice_total = self.invoice_total
		# Calculate subtotal
		for item in self.invoice_items:
			invoice_total += item.item_total
		self.invoice_total = invoice_total
		return self.invoice_total
			

# Make a separate class for each invoice item
class invoice_item:
	def __init__(self, item_description, item_cost, item_quantity, item_total):
		self.item_description = item_description
		self.item_cost = float(item_cost)
		self.item_quantity = float(item_quantity)
		self.item_total = float(item_total)



############################################### FUNCTIONS #############################################


# Manually generate the invoice and items

def generate_invoice_manually():

	invoice_inputs = []
	invoice_items = []
	invoice_item_inputs = []


	# Gather Invoice Information
	invoice_inputs.append(input("Invoice number: "))
	invoice_inputs.append(input("Company: "))
	invoice_inputs.append(input("Company Address: "))
	invoice_inputs.append(input("Date Drafted: "))
	invoice_inputs.append(input("Bill To Company: "))
	invoice_inputs.append(input("Bill To Company Address: "))
	invoice_inputs.append(input("Product Description: "))
	invoice_inputs.append(input("Payment Due Date: "))
	invoice_inputs.append(input("Payment Method: "))

	# Initialize the invoice
	invoice_gen = invoice( \
		invoice_inputs[0], \
		invoice_inputs[1], \
		invoice_inputs[2], \
		invoice_inputs[3], \
		invoice_inputs[4], \
		invoice_inputs[5], \
		invoice_inputs[6], \
		invoice_inputs[7], \
		invoice_inputs[8], \
		invoice_inputs[9] \
		)

	# Gather all items and add them to the invoice
	num_items = input("Number of invoice items: ")
	for num in num_items:
		# Gather item inputs
		invoice_item_inputs.append(input("Item Description: "))
		invoice_item_inputs.append(float(input("Item Cost: ")))
		invoice_item_inputs.append(float(input("Item Quantity: ")))
		invoice_item_inputs.append(invoice_item_inputs[1]*invoice_item_inputs[2])

		# Initialize the item
		item = invoice_item(invoice_item_inputs[0],invoice_item_inputs[1],invoice_item_inputs[2],invoice_item_inputs[3])

		# Add the item to the invoice
		invoice_gen.add_item(item)

	# Total up the invoice
	invoice_gen.calculate_totals()


	return invoice_gen

# Import invoice info and items from CSV

def generate_invoice_from_CSV_upload(CSV_path):
	return


##################################### TESTING CODE #############################

######### TEST THE INVOICE CLASSES CODE ##########
# test_invoice = invoice(1, "Nate", "1234 Gill Road Skokie, IL 60076", "03/12/2019", "Mom", "123 Gill Rd Skokie, IL 60076", "Eat Creativ", "03/15/2019", "Check payable to Nate")

# test_item = invoice_item("FedEx shipping cost", 12, 1, 12)

# # print(test_item.item_cost)

# test_invoice.add_item(test_item)
# test_invoice.calculate_totals()

# print(test_invoice.invoice_total)


####### TEST THE INVOICE GENERATOR FUNCTIONS ########

# test_invoice = generate_invoice_manually()
# print(test_invoice.invoice_total)