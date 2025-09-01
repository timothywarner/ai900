#!/usr/bin/env python3
"""
Azure AI Document Intelligence Demo (formerly Form Recognizer)
=============================================================

This demo shows how to extract structured data from invoices using 
Azure AI Document Intelligence. Perfect for automating document processing!

Prerequisites:
    pip install azure-ai-formrecognizer
    pip install python-dotenv

Azure Setup:
    1. Create Document Intelligence resource in Azure Portal
    2. Get endpoint and key from Keys and Endpoint section
    3. Update credentials below or use .env file

What this demo covers:
    - Analyzing invoices with prebuilt models
    - Extracting vendor info, dates, line items, totals
    - Handling multiple invoice formats
    - Converting unstructured documents to structured data

AI-102 Connection:
    This bridges to AI-102 where you'll create custom models,
    handle complex documents, and build production pipelines.
"""

import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# Load configuration from environment variables
ENDPOINT = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
KEY = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_KEY")

# Validate environment variables
if not ENDPOINT or not KEY:
    print("❌ Error: Missing required environment variables!")
    print("Please set the following environment variables:")
    print("  - AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
    print("  - AZURE_DOCUMENT_INTELLIGENCE_KEY")
    print("\nRefer to tim-env.txt for setup instructions.")
    exit(1)


def analyze_invoice(invoice_path):
    """
    Analyze an invoice using the prebuilt invoice model.
    
    Args:
        invoice_path: Path to invoice file (PDF, JPEG, PNG, TIFF)
    """
    
    # Create client
    document_analysis_client = DocumentAnalysisClient(
        endpoint=ENDPOINT, 
        credential=AzureKeyCredential(KEY)
    )
    
    # Read invoice file
    with open(invoice_path, "rb") as invoice:
        print(f"\n📄 Analyzing invoice: {os.path.basename(invoice_path)}")
        print("=" * 60)
        
        # Start analysis
        poller = document_analysis_client.begin_analyze_document(
            model_id="prebuilt-invoice", 
            document=invoice
        )
        
        # Get results
        result = poller.result()
        
        # Process each invoice in the document
        for idx, invoice in enumerate(result.documents):
            print(f"\n🧾 Invoice #{idx + 1}")
            print("-" * 40)
            
            # Vendor information
            vendor_name = invoice.fields.get("VendorName")
            if vendor_name:
                print(f"Vendor: {vendor_name.value}")
                
            vendor_address = invoice.fields.get("VendorAddress")
            if vendor_address:
                print(f"Vendor Address: {vendor_address.value}")
            
            # Customer information
            customer_name = invoice.fields.get("CustomerName")
            if customer_name:
                print(f"Customer: {customer_name.value}")
            
            # Invoice details
            invoice_id = invoice.fields.get("InvoiceId")
            if invoice_id:
                print(f"Invoice ID: {invoice_id.value}")
                
            invoice_date = invoice.fields.get("InvoiceDate")
            if invoice_date:
                print(f"Invoice Date: {invoice_date.value}")
                
            due_date = invoice.fields.get("DueDate")
            if due_date:
                print(f"Due Date: {due_date.value}")
            
            # Financial information
            subtotal = invoice.fields.get("SubTotal")
            if subtotal:
                print(f"\nSubtotal: ${subtotal.value}")
                
            tax = invoice.fields.get("TotalTax")
            if tax:
                print(f"Tax: ${tax.value}")
                
            total = invoice.fields.get("InvoiceTotal")
            if total:
                print(f"Total: ${total.value}")
                
            # Line items
            items = invoice.fields.get("Items")
            if items:
                print("\n📦 Line Items:")
                print("-" * 40)
                for item in items.value:
                    description = item.value.get("Description")
                    quantity = item.value.get("Quantity")
                    unit_price = item.value.get("UnitPrice")
                    amount = item.value.get("Amount")
                    
                    if description:
                        print(f"\n  {description.value}")
                        if quantity:
                            print(f"    Quantity: {quantity.value}")
                        if unit_price:
                            print(f"    Unit Price: ${unit_price.value}")
                        if amount:
                            print(f"    Amount: ${amount.value}")


def analyze_receipt(receipt_path):
    """
    Analyze a receipt using the prebuilt receipt model.
    Great for expense tracking!
    """
    
    document_analysis_client = DocumentAnalysisClient(
        endpoint=ENDPOINT, 
        credential=AzureKeyCredential(KEY)
    )
    
    with open(receipt_path, "rb") as receipt:
        print(f"\n🧾 Analyzing receipt: {os.path.basename(receipt_path)}")
        print("=" * 60)
        
        poller = document_analysis_client.begin_analyze_document(
            model_id="prebuilt-receipt", 
            document=receipt
        )
        
        result = poller.result()
        
        for idx, receipt in enumerate(result.documents):
            print(f"\nReceipt #{idx + 1}")
            print("-" * 40)
            
            # Merchant info
            merchant = receipt.fields.get("MerchantName")
            if merchant:
                print(f"Merchant: {merchant.value}")
                
            merchant_address = receipt.fields.get("MerchantAddress")
            if merchant_address:
                print(f"Address: {merchant_address.value}")
                
            # Transaction details
            transaction_date = receipt.fields.get("TransactionDate")
            if transaction_date:
                print(f"Date: {transaction_date.value}")
                
            # Items
            items = receipt.fields.get("Items")
            if items:
                print("\nItems:")
                for item in items.value:
                    name = item.value.get("Name")
                    price = item.value.get("Price")
                    if name and price:
                        print(f"  - {name.value}: ${price.value}")
            
            # Totals
            subtotal = receipt.fields.get("Subtotal")
            if subtotal:
                print(f"\nSubtotal: ${subtotal.value}")
                
            tax = receipt.fields.get("TotalTax")
            if tax:
                print(f"Tax: ${tax.value}")
                
            total = receipt.fields.get("Total")
            if total:
                print(f"Total: ${total.value}")


def main():
    """
    Demo Document Intelligence with various document types.
    """
    
    print("🤖 Azure AI Document Intelligence Demo")
    print("=" * 60)
    print("Extracting structured data from documents...\n")
    
    # Base path for assets
    assets_path = "../../assets/OCR"
    
    # Demo 1: Analyze invoices
    invoice_files = [
        "Invoice_1.pdf",
        "Invoice_2.pdf"
    ]
    
    print("📋 INVOICE ANALYSIS")
    print("=" * 60)
    
    for invoice_file in invoice_files:
        invoice_path = os.path.join(assets_path, invoice_file)
        if os.path.exists(invoice_path):
            try:
                analyze_invoice(invoice_path)
            except Exception as e:
                print(f"❌ Error analyzing {invoice_file}: {str(e)}")
        else:
            print(f"⚠️  Invoice file not found: {invoice_path}")
    
    # Demo 2: Analyze receipts
    print("\n\n📋 RECEIPT ANALYSIS")
    print("=" * 60)
    
    receipt_files = [
        "contoso-receipt.png",
        "contoso-allinone-receipt.jpg"
    ]
    
    for receipt_file in receipt_files:
        receipt_path = os.path.join(assets_path, receipt_file)
        if os.path.exists(receipt_path):
            try:
                analyze_receipt(receipt_path)
            except Exception as e:
                print(f"❌ Error analyzing {receipt_file}: {str(e)}")
        else:
            print(f"⚠️  Receipt file not found: {receipt_path}")
    
    print("\n\n✅ Demo Complete!")
    print("-" * 60)
    print("🎯 Key Takeaways:")
    print("  - Document Intelligence extracts structured data from documents")
    print("  - Prebuilt models handle common document types (invoices, receipts)")
    print("  - No training required for standard document formats")
    print("  - AI-102 explores custom models for specialized documents")
    

if __name__ == "__main__":
    main()