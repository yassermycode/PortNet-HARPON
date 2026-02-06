import jsPDF from 'jspdf';
import autoTable from 'jspdf-autotable';

// Logo PortNet en Base64 - Version avec fond blanc (globe avec PORTNET)
const PORTNET_LOGO_BASE64 = 'data:image/png;base64,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';

// Charger le logo depuis le fichier (fallback si le base64 ne fonctionne pas)
let logoFromFile = null;

const loadLogoFromFile = async () => {
  if (logoFromFile) return logoFromFile;
  
  try {
    const response = await fetch('/portnet-logo.png');
    if (!response.ok) throw new Error('Logo non trouvé');
    const blob = await response.blob();
    return new Promise((resolve) => {
      const reader = new FileReader();
      reader.onloadend = () => {
        logoFromFile = reader.result;
        resolve(logoFromFile);
      };
      reader.readAsDataURL(blob);
    });
  } catch (error) {
    console.warn('Logo fichier non disponible:', error);
    return null;
  }
};

export const generateCaseReport = async (caseData, documents) => {
  // LOGS DE DEBUG
  console.log('Génération PDF...');
  console.log('Case data:', caseData);
  console.log('Documents:', documents);
  
  try {
    // Vérification des données
    if (!caseData) {
      console.error('Erreur: caseData est undefined');
      throw new Error('Données du dossier manquantes');
    }
    
    // Utiliser le logo base64 intégré ou charger depuis le fichier
    let logo = PORTNET_LOGO_BASE64;
    if (!logo) {
      logo = await loadLogoFromFile();
    }
    
    // Créer un nouveau document PDF
    const doc = new jsPDF();
    
    // Vérifier que autoTable est disponible
    console.log('autoTable disponible:', typeof doc.autoTable === 'function');
    
    // Assurer que documents est un tableau
    const safeDocuments = Array.isArray(documents) ? documents : [];
    
    let yPosition = 20;
    let logoAdded = false;
    
    // ========================================
    // EN-TÊTE DU RAPPORT AVEC LOGO
    // ========================================
    
    // Ajouter le logo PortNet centré en haut
    if (logo) {
      try {
        // Logo centré en haut du document
        doc.addImage(logo, 'PNG', 55, 8, 100, 30);
        logoAdded = true;
        yPosition = 42;
        console.log('Logo PortNet ajouté au PDF');
      } catch (e) {
        console.warn('Impossible d\'ajouter le logo:', e);
        logoAdded = false;
      }
    }
    
    // Sous-titre si logo ajouté
    if (logoAdded) {
      doc.setFontSize(10);
      doc.setTextColor(100, 100, 100);
      doc.setFont(undefined, 'normal');
      doc.text('Système d\'Analyse des Risques Douaniers', 105, yPosition, { align: 'center' });
      yPosition += 12;
    } else {
      // Titre principal sans logo
      doc.setFontSize(24);
      doc.setTextColor(35, 42, 86); // Bleu PortNet #232a56
      doc.setFont(undefined, 'bold');
      doc.text('PORTNET HARPON', 105, yPosition, { align: 'center' });
      yPosition += 8;
      
      doc.setFontSize(11);
      doc.setTextColor(100, 100, 100);
      doc.setFont(undefined, 'normal');
      doc.text('Système d\'Analyse des Risques Douaniers', 105, yPosition, { align: 'center' });
      yPosition += 12;
    }
    
    // Titre du rapport
    doc.setFontSize(18);
    doc.setTextColor(35, 42, 86);
    doc.setFont(undefined, 'bold');
    doc.text('Rapport d\'Analyse de Dossier', 105, yPosition, { align: 'center' });
    
    yPosition += 10;
    
    // Ligne de séparation
    doc.setDrawColor(35, 42, 86);
    doc.setLineWidth(0.5);
    doc.line(20, yPosition, 190, yPosition);
    
    yPosition += 10;
    
    // ========================================
    // INFORMATIONS DU DOSSIER
    // ========================================
    
    doc.setFontSize(12);
    doc.setTextColor(0, 0, 0);
    doc.setFont(undefined, 'normal');
    
    doc.text(`Référence: ${caseData.reference_id || caseData.case_number || 'N/A'}`, 20, yPosition);
    yPosition += 7;
    
    doc.text(`Date de création: ${caseData.created_at ? new Date(caseData.created_at).toLocaleDateString('fr-FR') : 'N/A'}`, 20, yPosition);
    yPosition += 7;
    
    doc.text(`Statut: ${caseData.status || 'N/A'}`, 20, yPosition);
    yPosition += 7;
    
    // Score de risque avec couleur
    const riskScore = caseData.risk_score || caseData.global_risk_score || 0;
    const riskLevel = riskScore >= 70 ? 'ÉLEVÉ' : riskScore >= 40 ? 'MOYEN' : 'FAIBLE';
    const riskColor = riskScore >= 70 ? [220, 38, 38] : riskScore >= 40 ? [245, 158, 11] : [34, 197, 94];
    
    doc.text('Score de risque: ', 20, yPosition);
    doc.setTextColor(...riskColor);
    doc.setFont(undefined, 'bold');
    doc.text(`${riskScore}% (${riskLevel})`, 55, yPosition);
    doc.setTextColor(0, 0, 0);
    doc.setFont(undefined, 'normal');
    
    yPosition += 15;
    
    // ========================================
    // DOCUMENTS ANALYSÉS
    // ========================================
    
    doc.setFontSize(14);
    doc.setTextColor(35, 42, 86);
    doc.setFont(undefined, 'bold');
    doc.text('Documents Analysés', 20, yPosition);
    yPosition += 8;
    
    if (safeDocuments.length > 0) {
      const docTableData = safeDocuments.map((docItem, index) => [
        index + 1,
        docItem.filename || docItem.name || 'Document',
        docItem.doc_type || docItem.document_type || 'Non classé',
        docItem.risk_score !== undefined ? `${docItem.risk_score}%` : 'N/A'
      ]);
      
      autoTable(doc, {
        startY: yPosition,
        head: [['#', 'Nom du fichier', 'Type', 'Risque']],
        body: docTableData,
        theme: 'striped',
        headStyles: { 
          fillColor: [35, 42, 86],
          textColor: [255, 255, 255],
          fontStyle: 'bold'
        },
        alternateRowStyles: { fillColor: [245, 247, 250] },
        margin: { left: 20, right: 20 }
      });
      
      yPosition = doc.lastAutoTable.finalY + 15;
    } else {
      doc.setFontSize(11);
      doc.setTextColor(100, 100, 100);
      doc.setFont(undefined, 'italic');
      doc.text('Aucun document analysé', 20, yPosition);
      yPosition += 15;
    }
    
    // ========================================
    // SIGNAUX DE RISQUE
    // ========================================
    
    if (yPosition > 250) {
      doc.addPage();
      yPosition = 20;
    }
    
    doc.setFontSize(14);
    doc.setTextColor(35, 42, 86);
    doc.setFont(undefined, 'bold');
    doc.text('Signaux de Risque Détectés', 20, yPosition);
    yPosition += 8;
    
    const signals = caseData.signals || caseData.risk_signals || [];
    
    if (signals.length > 0) {
      const signalTableData = signals.map((signal, index) => {
        const severity = signal.severity || signal.level || 'medium';
        const severityLabel = severity === 'high' ? 'Élevé' : severity === 'medium' ? 'Moyen' : 'Faible';
        return [
          index + 1,
          signal.signal_type || signal.type || 'Signal',
          signal.description || signal.message || '-',
          severityLabel
        ];
      });
      
      autoTable(doc, {
        startY: yPosition,
        head: [['#', 'Type', 'Description', 'Sévérité']],
        body: signalTableData,
        theme: 'striped',
        headStyles: { 
          fillColor: [35, 42, 86],
          textColor: [255, 255, 255],
          fontStyle: 'bold'
        },
        alternateRowStyles: { fillColor: [245, 247, 250] },
        margin: { left: 20, right: 20 },
        columnStyles: {
          2: { cellWidth: 80 }
        }
      });
      
      yPosition = doc.lastAutoTable.finalY + 15;
    } else {
      doc.setFontSize(11);
      doc.setTextColor(34, 197, 94);
      doc.setFont(undefined, 'normal');
      doc.text('Aucun signal de risque détecté', 20, yPosition);
      yPosition += 15;
    }
    
    // ========================================
    // AIDE À LA DÉCISION
    // ========================================
    
    if (yPosition > 250) {
      doc.addPage();
      yPosition = 20;
    }
    
    doc.setFontSize(14);
    doc.setTextColor(35, 42, 86);
    doc.setFont(undefined, 'bold');
    doc.text('Aide à la Décision', 20, yPosition);
    yPosition += 10;
    
    // Niveau de risque global
    doc.setFontSize(12);
    doc.setFont(undefined, 'normal');
    doc.setTextColor(0, 0, 0);
    doc.text('Niveau de risque global: ', 20, yPosition);
    doc.setTextColor(...riskColor);
    doc.setFont(undefined, 'bold');
    doc.text(riskLevel, 70, yPosition);
    yPosition += 10;
    
    // Recommandation
    doc.setTextColor(0, 0, 0);
    doc.setFont(undefined, 'normal');
    let recommendation = '';
    if (riskScore >= 70) {
      recommendation = 'Contrôle approfondi recommandé. Ce dossier présente des indicateurs de risque significatifs nécessitant une attention particulière.';
    } else if (riskScore >= 40) {
      recommendation = 'Contrôle standard recommandé. Quelques points d\'attention ont été identifiés.';
    } else {
      recommendation = 'Risque faible. Le dossier peut être traité selon la procédure standard.';
    }
    
    const recLines = doc.splitTextToSize(recommendation, 170);
    doc.text(recLines, 20, yPosition);
    yPosition += (recLines.length * 6) + 10;
    
    // ========================================
    // RECOMMANDATIONS SPÉCIFIQUES
    // ========================================
    
    const recommendations = caseData.recommendations || [];
    
    if (recommendations.length > 0 && yPosition < 250) {
      doc.setFontSize(14);
      doc.setTextColor(35, 42, 86);
      doc.setFont(undefined, 'bold');
      doc.text('Recommandations Spécifiques', 20, yPosition);
      yPosition += 8;
      
      doc.setFontSize(11);
      doc.setTextColor(0, 0, 0);
      doc.setFont(undefined, 'normal');
      
      recommendations.forEach((rec, index) => {
        if (yPosition > 280) {
          doc.addPage();
          yPosition = 20;
        }
        
        const lines = doc.splitTextToSize(`${index + 1}. ${rec}`, 170);
        doc.text(lines, 20, yPosition);
        yPosition += (lines.length * 5) + 3;
      });
    }
    
    // ========================================
    // PIED DE PAGE AVEC LOGO
    // ========================================
    
    const pageCount = doc.internal.getNumberOfPages();
    
    for (let i = 1; i <= pageCount; i++) {
      doc.setPage(i);
      
      // Ligne de séparation footer
      doc.setDrawColor(35, 42, 86);
      doc.setLineWidth(0.3);
      doc.line(20, 280, 190, 280);
      
      // Logo mini en footer si disponible
      if (logoAdded && logo) {
        try {
          doc.addImage(logo, 'PNG', 15, 281, 35, 12);
        } catch (e) {
          // Ignorer si le logo ne peut pas être ajouté
        }
      }
      
      doc.setFontSize(8);
      doc.setTextColor(35, 42, 86);
      doc.setFont(undefined, 'bold');
      doc.text('PORTNET HARPON', logoAdded ? 55 : 20, 286);
      
      doc.setTextColor(100, 100, 100);
      doc.setFont(undefined, 'normal');
      doc.text('Guichet Unique - Système d\'Analyse des Risques Douaniers', logoAdded ? 55 : 20, 290);
      
      // Date de génération
      doc.text(
        `Généré le ${new Date().toLocaleDateString('fr-FR')} à ${new Date().toLocaleTimeString('fr-FR')}`,
        105,
        295,
        { align: 'center' }
      );
      
      // Numéro de page
      doc.text(
        `Page ${i} / ${pageCount}`,
        190,
        290,
        { align: 'right' }
      );
    }
    
    // ========================================
    // TÉLÉCHARGEMENT
    // ========================================
    
    console.log('PDF généré avec succès');
    
    const filename = `${caseData.reference_id || caseData.case_number || 'rapport'}_${new Date().toISOString().split('T')[0]}.pdf`;
    doc.save(filename);
    
    return filename;
    
  } catch (error) {
    console.error('Erreur génération PDF:', error);
    console.error('Stack:', error.stack);
    throw new Error(`Erreur lors de la génération du PDF: ${error.message}`);
  }
};
