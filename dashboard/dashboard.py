import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.header('E-commerce Public Dashboard :sparkles:')

customers_dataset_df = pd.read_csv(
    "dashboard/customers_dataset.csv")
geolocation_dataset_df = pd.read_csv(
    "dashboard/geolocation_dataset.csv")
order_items_dataset_df = pd.read_csv(
    "dashboard/order_items_dataset.csv")
order_payments_dataset_df = pd.read_csv(
    "dashboard/order_payments_dataset.csv")
order_reviews_dataset_df = pd.read_csv(
    "dashboard/order_reviews_dataset.csv")
orders_dataset_df = pd.read_csv(
    "dashboard/orders_dataset.csv")
product_category_name_translation_df = pd.read_csv(
    "dashboard/product_category_name_translation.csv")
products_dataset_df = pd.read_csv(
    "dashboard/products_dataset.csv")
sellers_dataset_df = pd.read_csv(
    "dashboard/sellers_dataset.csv")

st.subheader("Customer Demographics")

bystate_df = customers_dataset_df.groupby(
    by="customer_state").customer_id.nunique().reset_index()
bystate_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
bystate_df
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3",
          "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="customer_count",
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Number of Customer by States", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)


st.subheader("Best & Worst Payment Type")
bypayment_df = order_payments_dataset_df.groupby(
    by="payment_type").order_id.nunique().reset_index()
bypayment_df.rename(columns={
    "order_id": "order_count"
}, inplace=True)
bypayment_df
fig, ax = plt.subplots(figsize=(10, 5))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3",
          "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="order_count",
    y="payment_type",
    data=bypayment_df.sort_values(by="order_count", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Number of Customer by States", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)
