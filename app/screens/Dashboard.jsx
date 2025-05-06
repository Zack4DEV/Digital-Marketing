import React from 'react';
import { View, ScrollView, StyleSheet } from 'react-native';
import { Card, Title, Text } from 'react-native-paper';
import { LineChart } from 'react-native-chart-kit';
import AIAssistant from '../components/AIAssistant';

const Dashboard = () => {
  const campaignData = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [{
      data: [20, 45, 28, 80, 99, 43],
    }]
  };

  return (
    <ScrollView style={styles.container}>
      <AIAssistant />
      
      <Card style={styles.card}>
        <Card.Content>
          <Title>Campaign Performance</Title>
          <LineChart
            data={campaignData}
            width={300}
            height={220}
            chartConfig={{
              backgroundColor: '#ffffff',
              backgroundGradientFrom: '#ffffff',
              backgroundGradientTo: '#ffffff',
              decimalPlaces: 0,
              color: (opacity = 1) => `rgba(81, 150, 244, ${opacity})`,
              labelColor: () => '#333',
            }}
            bezier
            style={styles.chart}
          />
        </Card.Content>
      </Card>

      <View style={styles.statsContainer}>
        <Card style={styles.statsCard}>
          <Card.Content>
            <Title>Engagement Rate</Title>
            <Text>4.8%</Text>
          </Card.Content>
        </Card>

        <Card style={styles.statsCard}>
          <Card.Content>
            <Title>Reach</Title>
            <Text>50.2K</Text>
          </Card.Content>
        </Card>
      </View>

      <Card style={styles.card}>
        <Card.Content>
          <Title>Active Campaigns</Title>
          <Text>Summer Collection Launch</Text>
          <Text>Fitness Challenge</Text>
          <Text>Tech Review Series</Text>
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
  chart: {
    marginVertical: 8,
    borderRadius: 16,
  },
  statsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 16,
  },
  statsCard: {
    width: '48%',
    elevation: 4,
  },
});

export default Dashboard;