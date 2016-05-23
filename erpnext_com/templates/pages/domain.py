import frappe

def get_context(context):
	context.no_cache = True
	context.update({"erpnext_page": get_erpnext_page(page_name = frappe.form_dict.name)})
	subsite = frappe.get_doc('Subsite', context.erpnext_page.subsite)
	context.brand_html = subsite.brand_html
	context.sub_navbar_items = subsite.sub_navbar_items

@frappe.whitelist(allow_guest=True)
def get_erpnext_page(page_name):
	erpnext_page = frappe.get_doc('ERPNext Page', page_name).as_dict()
	erpnext_page.fullfeatures = []
	erpnext_page.gridfeatures = []
	for f in erpnext_page.full_section:
		erpnext_page.fullfeatures.append(frappe.get_all('ERPNext Feature',filters={'name':f.features},
		fields=["feature_headline", "feature_sub_headline", "image", "article"]))
	for f in erpnext_page.grid_section:
		erpnext_page.gridfeatures.append(frappe.get_all('ERPNext Feature',filters={'name':f.features},
		fields=["feature_headline", "feature_sub_headline", "image", "article"]))
	return erpnext_page