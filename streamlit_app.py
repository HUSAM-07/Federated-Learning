import streamlit as st
import plotly.graph_objects as go

# Data for the classifiers
data = {
    "33 Class Classifier": {
        "clients": [5, 10, 15],
        "accuracy": [0.97, 0.955, 0.85],
        "loss": [0.07, 0.15, 0.35]
    },
    "7 Class Classifier": {
        "clients": [5, 10],
        "accuracy": [0.9833, 0.9781],
        "loss": [0.0541, 0.0731]
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
    st.set_page_config(page_icon="🚦",initial_sidebar_state="expanded",page_title="Federated Learning for IoT")

    st.markdown(""">Made by Mohammed Husamuddin
                *Mentor: Dr. Pranav M Pawar""")


    menu = st.sidebar.selectbox("Choose a page", ["Visualization", "Federated Learning Info"])

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

if __name__ == "__main__":
    main()
