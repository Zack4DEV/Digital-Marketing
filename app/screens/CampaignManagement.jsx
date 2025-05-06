import React, { useState } from 'react';
import { View, ScrollView, StyleSheet } from 'react-native';
import { Card, Title, Button, TextInput, DataTable } from 'react-native-paper';

const CampaignManagement = () => {
  const [campaigns] = useState([
    {
      id: 1,
      name: 'Summer Collection',
      status: 'Active',
      reach: '50K',
      engagement: '4.8%',
    },
    {
      id: 2,
      name: 'Fitness Challenge',
      status: 'Active',
      reach: '30K',
      engagement: '3.2%',
    },
    {
      id: 3,
      name: 'Tech Reviews',
      status: 'Planned',
      reach: '0',
      engagement: '0%',
    },
  ]);

  return (
    <ScrollView style={styles.container}>
      <Card style={styles.card}>
        <Card.Content>
          <Title>Create New Campaign</Title>
          <TextInput
            label="Campaign Name"
            mode="outlined"
            style={styles.input}
          />
          <TextInput
            label="Description"
            mode="outlined"
            multiline
            numberOfLines={3}
            style={styles.input}
          />
          <TextInput
            label="Target Audience"
            mode="outlined"
            style={styles.input}
          />
          <Button mode="contained" style={styles.button}>
            Create Campaign
          </Button>
        </Card.Content>
      </Card>

      <Card style={styles.card}>
        <Card.Content>
          <Title>Active Campaigns</Title>
          <DataTable>
            <DataTable.Header>
              <DataTable.Title>Name</DataTable.Title>
              <DataTable.Title>Status</DataTable.Title>
              <DataTable.Title numeric>Reach</DataTable.Title>
              <DataTable.Title numeric>Engagement</DataTable.Title>
            </DataTable.Header>

            {campaigns.map((campaign) => (
              <DataTable.Row key={campaign.id}>
                <DataTable.Cell>{campaign.name}</DataTable.Cell>
                <DataTable.Cell>{campaign.status}</DataTable.Cell>
                <DataTable.Cell numeric>{campaign.reach}</DataTable.Cell>
                <DataTable.Cell numeric>{campaign.engagement}</DataTable.Cell>
              </DataTable.Row>
            ))}
          </DataTable>
        </Card.Content>
      </Card>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#f5f5f5',
  },
  card: {
    marginBottom: 16,
    elevation: 4,
  },
  input: {
    marginBottom: 12,
  },
  button: {
    marginTop: 8,
  },
});

export default CampaignManagement;