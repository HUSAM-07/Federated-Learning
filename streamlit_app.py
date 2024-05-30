import streamlit as st
import plotly.graph_objects as go
import time

# Set page configuration
st.set_page_config(page_icon="🚦", initial_sidebar_state="expanded", page_title="Federated Learning for IoT")

# Markdown header
st.markdown(""">Made by Mohammed Husamuddin | Mentor: Dr. Pranav M Pawar""")

# Data for the classifiers
data = {
    "33 Class Classifier": {
        "clients": [5, 10, 15],
        "accuracy": [0.97, 0.955, 0.85],
        "loss": [0.07, 0.15, 0.35]
    },
    "7 Class Classifier": {
        "clients": [5, 10, 15],
        "accuracy": [0.9833, 0.9781, 0.854656],
        "loss": [0.0541, 0.0731, 0.342776]
    }
}

# Labels for the classifiers
labels_33 = [
    {"Category": "Benign Traffic", "Attack Name": "Benign Traffic", "Label": 0},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-RSTFINFlood", "Label": 1},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-PSHACK_Flood", "Label": 2},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-SYN_Flood", "Label": 3},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-UDP_Flood", "Label": 4},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-TCP_Flood", "Label": 5},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-ICMP_Flood", "Label": 6},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-SynonymousIP_Flood", "Label": 7},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-ACK_Fragmentation", "Label": 8},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-UDP_Fragmentation", "Label": 9},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-ICMP_Fragmentation", "Label": 10},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-SlowLoris", "Label": 11},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-HTTP_Flood", "Label": 12},
    {"Category": "DDoS and DoS", "Attack Name": "DoS-UDP_Flood", "Label": 13},
    {"Category": "DDoS and DoS", "Attack Name": "DoS-SYN_Flood", "Label": 14},
    {"Category": "DDoS and DoS", "Attack Name": "DoS-TCP_Flood", "Label": 15},
    {"Category": "DDoS and DoS", "Attack Name": "DoS-HTTP_Flood", "Label": 16},
    {"Category": "Mirai", "Attack Name": "Mirai-greeth_flood", "Label": 17},
    {"Category": "Mirai", "Attack Name": "Mirai-greip_flood", "Label": 18},
    {"Category": "Mirai", "Attack Name": "Mirai-udpplain", "Label": 19},
    {"Category": "Reconnaissance", "Attack Name": "Recon-PingSweep", "Label": 20},
    {"Category": "Reconnaissance", "Attack Name": "Recon-OSScan", "Label": 21},
    {"Category": "Reconnaissance", "Attack Name": "Recon-PortScan", "Label": 22},
    {"Category": "Reconnaissance", "Attack Name": "VulnerabilityScan", "Label": 23},
    {"Category": "Reconnaissance", "Attack Name": "Recon-HostDiscovery", "Label": 24},
    {"Category": "Spoofing", "Attack Name": "DNS_Spoofing", "Label": 25},
    {"Category": "Spoofing", "Attack Name": "MITM-ArpSpoofing", "Label": 26},
    {"Category": "Web", "Attack Name": "BrowserHijacking", "Label": 27},
    {"Category": "Web", "Attack Name": "Backdoor_Malware", "Label": 28},
    {"Category": "Web", "Attack Name": "XSS", "Label": 29},
    {"Category": "Web", "Attack Name": "Uploading_Attack", "Label": 30},
    {"Category": "Web", "Attack Name": "SqlInjection", "Label": 31},
    {"Category": "Web", "Attack Name": "CommandInjection", "Label": 32},
    {"Category": "Other", "Attack Name": "DictionaryBruteForce", "Label": 33},
]

labels_7 = [
    {"Category": "Benign Traffic", "Attack Name": "Benign Traffic", "Label": 0},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-RSTFINFlood", "Label": 1},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-PSHACK_Flood", "Label": 2},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-SYN_Flood", "Label": 3},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-UDP_Flood", "Label": 4},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-TCP_Flood", "Label": 5},
    {"Category": "DDoS and DoS", "Attack Name": "DDoS-ICMP_Flood", "Label": 6}
]

def plot_metrics(classifier_type, clients, accuracy, loss):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=clients, y=accuracy, mode='lines+markers', name='Accuracy'))
    fig.add_trace(go.Scatter(x=clients, y=loss, mode='lines+markers', name='Loss'))

    fig.update_layout(
        title=f'Accuracy and Loss for {classifier_type}',
        xaxis_title='Number of Clients',
        yaxis_title='Value',
        legend_title='Metrics',
        template='plotly_dark'
    )
    return fig

def display_labels(labels):
    st.table(labels)

def main():
    st.title("Federated Learning Classifier Dashboard")

    menu = st.sidebar.selectbox("Choose a page", ["Visualization", "Federated Learning Info", "FL Process Visualization"])

    if menu == "Visualization":
        st.sidebar.header("Visualization Settings")
        classifier_type = st.sidebar.selectbox("Select Classifier", ["7 Class Classifier", "33 Class Classifier"])
        num_clients = st.sidebar.selectbox("Number of Clients", [5, 10, 15])

        # Update data based on classifier type
        data_classifier = data[classifier_type]
        
        if num_clients not in data_classifier["clients"]:
            st.error(f"Data for {num_clients} clients is not available for the {classifier_type}. Please select another number of clients.")
        else:
            fig = plot_metrics(
                classifier_type,
                data_classifier["clients"],
                data_classifier["accuracy"],
                data_classifier["loss"]
            )
            st.plotly_chart(fig)

    elif menu == "Federated Learning Info":
        st.header("Federated Learning")
        st.write("""
        Federated learning is a machine learning technique that trains an algorithm across multiple decentralized devices or servers holding local data samples, without exchanging them. 
        This approach contrasts with traditional centralized machine learning techniques where all local datasets are uploaded to one server, as well as more classical decentralized approaches which often assume that local data samples are identically distributed.
        """)

        st.subheader("7 Class Classifier Labels")
        display_labels(labels_7)

        st.subheader("33 Class Classifier Labels")
        display_labels(labels_33)

    elif menu == "FL Process Visulaization":

        # Define the layout and elements of the diagram
        st.title("Federated Learning System Visualization")

        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.header("Strategy")
            configure_train_eval = st.empty()
            configure_train_eval.code("Configure\ntrain/eval", language="python")

        with col2:
            st.header(" ")
            global_model = st.empty()
            global_model.code("Global\nModel", language="python")

        with col3:
            st.header(" ")
            configure_train_eval_2 = st.empty()
            configure_train_eval_2.code("Configure\ntrain/eval", language="python")

        # Create placeholders for dynamic elements
        client_manager = st.empty()
        rpc_server = st.empty()

        # Function to draw arrows
        def draw_arrow(container, start_col, end_col, color="blue", text=""):
            with container:
                if start_col < end_col:
                    st.markdown(f"<div style='text-align: center;'><span style='font-size:24px; color:{color};'>→ {text}</span></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='text-align: center;'><span style='font-size:24px; color:{color};'>{text} ←</span></div>", unsafe_allow_html=True)


        # Function to visualize a client
        def visualize_client(container, client_type, client_status="active"):
            with container:
                st.code(f"{client_type.upper()}\nClient\nProxy", language="python")
                if client_type == "edge":
                    st.code("RPC Client\n\nTraining\nPipeline\n\nData\n\nEdge Client", language="python")
                else:
                    status_text = "(inactive)" if client_status == "inactive" else "(active)"
                    st.code(
                        f"Training\nPipeline\n\nData\n\nVirtual\nClient\n{status_text}",
                        language="python",
                    )


        # Draw the initial state of the system
        client_manager.header("Client\nManager")
        rpc_server.header("RPC\nServer")
        col1, col2, col3 = st.columns([1, 1, 1])
        visualize_client(col1, "edge")
        visualize_client(col2, "virtual", client_status="inactive")
        visualize_client(col3, "virtual")
        draw_arrow(st.container(), 1, 2, color="green", text="Model Update")
        draw_arrow(st.container(), 2, 3, color="green")
        draw_arrow(st.container(), 3, 2, color="blue", text="Aggregated Updates")
        draw_arrow(st.container(), 2, 1, color="blue")

        # Simulate the federated learning process
        for i in range(3):
            # Step 1: Send model to clients
            with st.spinner(f"Iteration {i+1}: Sending global model to clients..."):
                time.sleep(1)
            draw_arrow(st.container(), 1, 2, color="green", text="Model Update")
            draw_arrow(st.container(), 2, 3, color="green")
            time.sleep(1)

            # Step 2: Clients train locally
            with st.spinner("Clients training locally..."):
                time.sleep(2)

            # Step 3: Send updates back to server
            with st.spinner("Sending local updates to server..."):
                time.sleep(1)
            draw_arrow(st.container(), 3, 2, color="blue", text="Aggregated Updates")
            draw_arrow(st.container(), 2, 1, color="blue")
            time.sleep(1)

            # Step 4: Server aggregates updates
            with st.spinner("Server aggregating updates..."):
                time.sleep(1)

        # Display final results
        st.success("Federated Learning process complete!")

if __name__ == "__main__":
    main()
