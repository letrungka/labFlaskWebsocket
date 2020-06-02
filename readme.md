```
# Topology
# refer to https://blog.jverkamp.com/2015/07/20/configuring-websockets-behind-an-aws-elb/

Webrower(websocket client) >>> AWS CLB (80 - enable proxy mode) >>> NGINX(80 - proxy_protocol to read header proxy  ) >>> FLASK(5000 - socket server)

# create policy
aws elb create-load-balancer-policy \
    --load-balancer-name lab1 \
    --policy-name lab1-proxy-protocol \
    --policy-type-name ProxyProtocolPolicyType \
    --policy-attributes AttributeName=ProxyProtocol,AttributeValue=True

# Enable
aws elb set-load-balancer-policies-for-backend-server \
    --load-balancer-name lab1 \
    --instance-port 80 \
    --policy-names lab1-proxy-protocol

# Verify

aws elb describe-load-balancers --load-balancer-name lab1

# Disable
aws elb set-load-balancer-policies-for-backend-server --load-balancer-name lab1 --instance-port 80 --policy-names "[]"

```
