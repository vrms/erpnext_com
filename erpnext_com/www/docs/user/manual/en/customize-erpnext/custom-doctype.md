<!-- add-breadcrumbs -->
# Custom Doctype

DocType or a Document Type is a tool to insert form in ERPNext. The forms like Sales Order,
Sales Invoices, Work Order are added as Doctype in the backend. Let's assume we are
creating a Custom Doctype for a Book.

Custom Doctype allows you to insert custom forms in ERPNext as per your requirement.

To create a new **DocType**, go to:

`Setup > Customize > Doctype > New`

#### DocType Detail

1. Module: Select module in which this Doctype should be placed.
1. Name: Specify a name for the new DocType
1. Is Child table: If this Doctype is to be inserted as table into another Doctype, like Item table
in the Sales Order Doctype, then you should check Is Child Table. Else no.
1. Is Single: If checked, this Doctype will become a single form, like Selling Setting, which user will
not be able to re-produce.
1. Custom?: This field will be checked by default when adding Custom Doctype.

<img alt="Doctype Basic" class="screenshot" src="{{docs_base_url}}/assets/img/setup/customize/doctype-basics.png">

#### Fields

In the Fields Table, you can add the fields (properties) of the DocType (Article).

Fields are much more than database columns, they can be:

1. Columns in the database
1. For Layout (section / column breaks)
1. Child tables (Table type field)
1. HTML
1. Actions (button)
1. Attachments or Images

<img alt="Doc fields" class="screenshot" src="{{docs_base_url}}/assets/img/setup/customize/Doctype-all-fields.png">

When you add fields, you need to enter the **Type**. **Label** is optional for Section Break and Column Break. **Name** (`fieldname`) is the name of the database table column.

You can also set other properties of the field like whether it is mandatory, read only etc.

#### Naming

In this section, you can define criteria based on which document for this doctype will be named. There are multiple criterion based on which document can be named, like naming based on the value in the specific field, or based on Naming Series, or based on value provided by the user in the prompt, which will be shown when saving document. In the following example, we are doing naming based on the value in the field **book_name**.

<img alt="Doctype Naming" class="screenshot" src="{{docs_base_url}}/assets/img/setup/customize/doctype-field-naming.png">

#### Permission

In this table, you should select roles and define permission roles for them for this Doctype.

<img alt="Doctype Permissions" class="screenshot" src="{{docs_base_url}}/assets/img/setup/customize/Doctype-permissions.png">

#### Save DocType

Click the "Save" button on the upper right to actually create the new DocType. At this step a new table and it's respective Columns will be added to your Database. If there are any logical erros in the Doctype you will be prompted for them and have to adjust those before you actually can Save the DocType. It is not possible to save a Custom Doctype in a Draft state, so the best approach would be to go save it incrementally when it get's complex. Solve the problems that will appear with each incremental step and extend the complexitz of a DocType step by step like this.

<img alt="Doctype Save" class="screenshot" src="{{docs_base_url}}/assets/img/setup/customize/Doctype-save.png">

#### DocType in System

To check this Doctype, open Module defined for this doctype. Since we have added Books doctype in the
Human Resource module, to access this doctype, go to:

`Human Resource > Document > Book`

<img alt="Doctype List" class="screenshot" src="{{docs_base_url}}/assets/img/setup/customize/Doctype-list-view.png">

#### Book master

Using the fields entered, following is the master one book.

<img alt="Doctype Form" class="screenshot" src="{{docs_base_url}}/assets/img/setup/customize/Doctype-book-added.png">

{next}
