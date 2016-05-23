import frappe, json

def make(context):
	context = frappe._dict(context)
	get_context(context)
	return frappe.render_template('templates/includes/structured_page.html', context)

def get_context(context):
	context.full_sections = []
	context.full_grid_sections = []

	for f in context.get('sections') or []:
		with open(frappe.get_app_path('erpnext_com', 'features', f + '.json'), 'r') as jsonfile:
			feature = json.loads(jsonfile.read())
		context.full_sections.append(feature)

	for f in context.get('grid_sections') or []:
		with open(frappe.get_app_path('erpnext_com', 'features', f + '.json'), 'r') as jsonfile:
			feature = json.loads(jsonfile.read())
		context.full_grid_sections.append(feature)


	with open(frappe.get_app_path('erpnext_com', 'sites', context.site + '.json'), 'r') as jsonfile:
		site = json.loads(jsonfile.read())
		context.update(site)
