
#!/bin/bash
# ------------------------------------------------------------------
# Script: OCI_Prov.sh
# Purpose: Automate provisioning of an OCI compute instance
# Author: Mark Collins swampy10@gmail.com
# ------
set -e  # Exit immediately if a command exits with a non-zero status

# --- Set Variables ---
COMPARTMENT_ID="ocid1.compartment.oc1..aaaaaaaaz3y64ea3qtesiubyfknzb3wyos7gddy4dmpcx6b3rwiiwvhbh6mq"
SUBNET_ID="ocid1.subnet.oc1.uk-london-1.aaaaaaaajgko2cryu7sy5yzeu6ovwb4lm7jwjwhbgltvtatpi2bvfka4mxwa"
IMAGE_ID="ocid1.image.oc1.uk-london-1.aaaaaaaalb2otkfkzdbrh2oxtemvi6cstbsfrcbtgejrjht7u3irsldhnuca"
SHAPE="VM.Standard.E2.1"
SSH_KEY_PATH="$HOME/.ssh/id_rsa.pub"
INSTANCE_NAME="AutoInstance-$(date +%Y%m%d%H%M%S)"

if [[ -z "$IMAGE_ID" || -z "$SHAPE" ]]; then
  echo "[-] ERROR: Could not retrieve valid image or shape."
  exit 1
fi


echo "[+] Using image: $IMAGE_ID"
echo "[+] Using shape: $SHAPE"


# --- Create Instance ---
echo "[+] Creating instance..."
INSTANCE_ID=$(oci compute instance launch \
  --compartment-id $COMPARTMENT_ID \
  --availability-domain "$(oci iam availability-domain list --compartment-id $COMPARTMENT_ID --query 'data[0].name' --raw-output)" \
  --shape $SHAPE \
  --subnet-id $SUBNET_ID \
  --image-id $IMAGE_ID \
  --display-name $INSTANCE_NAME \
  --metadata "{\"ssh_authorized_keys\": \"$(cat $SSH_KEY_PATH)\"}" \
  --wait-for-state RUNNING \
  --max-wait-seconds 600 \
  --wait-interval-seconds 10 \
  --query "data.id" --raw-output)

echo "[+] Instance created with ID: $INSTANCE_ID"

# --- Obtain Public IP ---
PUBLIC_IP=$(oci compute instance list-vnics --instance-id $INSTANCE_ID --query "data[0].\"public-ip\"" --raw-output)

echo "[+] Instance running at IP: $PUBLIC_IP"

# --- Run basic commands ---
echo "[+] Running setup commands..."

ssh -o StrictHostKeyChecking=no ubuntu@$PUBLIC_IP << EOF
sudo apt update -y && sudo apt upgrade -y
echo "Hello from Oracle Cloud! Your instance is up and running and all updates have been applied" | sudo tee /etc/motd
EOF

echo "[+] Setup Complete."