import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

def main():
    st.title("Supply Chain Optimization System")
    
    # Inventory Management Section
    st.header("Inventory Management")
    inventory_level = st.number_input("Current Inventory Level", min_value=0, value=50)
    threshold = st.number_input("Threshold Level", min_value=0, value=30)
    
    if st.button("Evaluate Inventory"):
        response = requests.post(f"{BACKEND_URL}/evaluate_inventory/", json={
            "inventory_level": inventory_level,
            "threshold": threshold
        })
        st.write("Decision:", response.json().get("decision"))
    
    # Supplier Selection Section
    st.header("Supplier Selection")
    suppliers = []
    for i in range(3):
        name = st.text_input(f"Supplier {i+1} Name", value=f"Supplier {i+1}")
        cost = st.number_input(f"Supplier {i+1} Cost", min_value=0.0, value=100.0)
        suppliers.append({"name": name, "cost": cost})
    
    if st.button("Select Best Supplier"):
        response = requests.post(f"{BACKEND_URL}/select_supplier/", json={"suppliers": suppliers})
        st.write("Best Supplier:", response.json().get("best_supplier"))
    
    # Transportation Optimization Section
    st.header("Transportation Optimization")
    options = []
    for i in range(3):
        route = st.text_input(f"Route {i+1} Name", value=f"Route {i+1}")
        time = st.number_input(f"Route {i+1} Time", min_value=0.0, value=5.0)
        options.append({"route": route, "time": time})
    
    if st.button("Optimize Transportation"):
        response = requests.post(f"{BACKEND_URL}/optimize_transportation/", json={"options": options})
        st.write("Best Route:", response.json().get("best_route"))

if __name__ == "__main__":
    main()
