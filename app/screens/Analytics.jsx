import React from 'react';
import { ScrollView, StyleSheet, Dimensions } from 'react-native';
import { Card, Title, Text } from 'react-native-paper';
import { LineChart, BarChart, PieChart } from 'react-native-chart-kit';

const Analytics = () => {
  const engagementData = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [{
      data: [30, 45, 28, 80, 99, 43, 50],
    }]
  };

  const audienceData = {
    labels: ['18-24', '25-34', '35-44', '45+'],
    datasets: [{
      data: [20, 45, 28, 15],
    }]
  };

  const platformData = [
    {
      name: 'Instagram',
      population: 45,
      color: '#C13584',
      legendFontColor: '#7F7F7F',
      legendFontSize: 12,
    },
    {
      name: 'TikTok',
      population: 30,
      color: '#000000',
      legendFontColor: '#7F7F7F',
      legendFontSize: 12,
    },
    {
      name: 'YouTube',
      population: 25,
      color: '#FF0000',
      legendFontColor: '#7F7F7F',
      legendFontSize: 12,
    },
  ];

  return (
    <ScrollView style={styles.container}>
      <Card style={styles.card}>
        <Card.Content>
          <Title>Weekly Engagement</Title>
          <LineChart
            data={engagementData}
            width={Dimensions.get('window').width - 64}
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

      <Card style={styles.card}>
        <Card.Content>
          <Title>Audience Age Distribution</Title>
          <BarChart
            data={audienceData}
            width={Dimensions.get('window').width - 64}
            height={220}
            chartConfig={{
              backgroundColor: '#ffffff',
              backgroundGradientFrom: '#ffffff',
              backgroundGradientTo: '#ffffff',
              decimalPlaces: 0,
              color: (opacity = 1) => `rgba(134, 65, 244, ${opacity})`,
              labelColor: () => '#333',
            }}
            style={styles.chart}
          />
        </Card.Content>
      </Card>

      <Card style={styles.card}>
        <Card.Content>
          <Title>Platform Distribution</Title>
          <PieChart
            data={platformData}
            width={Dimensions.get('window').width - 64}
            height={220}
            chartConfig={{
              color: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
            }}
            accessor="population"
            backgroundColor="transparent"
            paddingLeft="15"
            style={styles.chart}
          />
        </Card.Content>
      </Card>

      <Card style={styles.card}>
        <Card.Content>
          <Title>Key Metrics</Title>
          <Text>Total Followers: 125K</Text>
          <Text>Average Engagement Rate: 4.8%</Text>
          <Text>Content Performance Score: 8.5/10</Text>
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
});

export default Analytics;